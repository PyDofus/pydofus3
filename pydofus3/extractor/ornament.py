"""
render dofus ornaments
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Pattern, TypedDict

import numpy as np
import orjson
import UnityPy
from moviepy import CompositeVideoClip, ImageClip, ImageSequenceClip, VideoClip, concatenate_videoclips
from PIL import Image, ImageChops
from tqdm import tqdm
from UnityPy.enums import ClassIDType
from collections import defaultdict

from pydofus3.enum_data import TypeData, get_data_path, TypeDataOther
from pydofus3.extractor.data.tools import BetterContainer

if TYPE_CHECKING:
    from pydofus3.generated.stub.aa_standalonewindows64 import OrnamentInfo, Vector4f


class Pivot(TypedDict):
    x: float
    y: float


class WingPart(TypedDict):
    w: float
    h: float
    pivot: Pivot

class AnchorType(IntEnum):
    TOP = 0
    CENTER = 1
    BOTTOM = 2


class ColorSource(IntEnum):
    NONE = 0
    GUILD = 1
    GUILD_ICON = 2
    ALLIANCE = 3
    ALLIANCE_ICON = 4

DEFAULT_COLORS: dict[int, tuple[int, int, int]] = {
    ColorSource.GUILD: (156, 36, 36),
    ColorSource.GUILD_ICON: (222, 184, 82),
    ColorSource.ALLIANCE: (52, 84, 156),
    ColorSource.ALLIANCE_ICON: (200, 200, 210),
}


class PartName(StrEnum):
    BACKGROUND = 'bg'
    BOTTOM = 'y'
    LEFT = 'w'
    RIGHT = 'z'
    TOP = 'x'


@dataclass
class Bbox:
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0

    @staticmethod
    def compute_max_bbox(bboxes: list[Bbox]) -> Bbox:
        if not bboxes:
            return Bbox()

        min_x = min(b.x for b in bboxes)
        min_y = min(b.y for b in bboxes)
        max_x = max(b.x + b.w for b in bboxes)
        max_y = max(b.y + b.h for b in bboxes)

        return Bbox(min_x, min_y, max_x - min_x, max_y - min_y)


@dataclass
class PartElement:
    part_name: PartName
    path: str
    position: Vector4f | None = None
    duration: float = 0
    start: float = 0
    anchor: int | None = None
    colorable_back: bool | None = None
    tint: tuple[int, int, int] | None = None
    assets: list[Image.Image] = field(default_factory=list)

    def _load_asset(self, is_animated: int, container: BetterContainer) -> None:
        if is_animated:
            container_name = f'Assets/Content/Ornaments/Textures/Animated/{self.path}.png'
            asset_type = ClassIDType.Sprite
        else:
            container_name = f'Assets/Content/Ornaments/Textures/Static/{self.path}.png'
            asset_type = ClassIDType.Texture2D

        if not (assets := container.get_asset_type(container_name, asset_type)):
            raise FileNotFoundError(f'{asset_type.name} {container_name} not found')

        if is_animated:
            objs = [i.read() for i in assets]
            texture = objs[0].m_RD.texture.read().image
            if len(objs) == 1:
                self.assets = [self.resize(texture)]
                return
            objs.sort(key=lambda x: int(x.m_Name.split('_')[-1]))
            self.assets = [
                self.resize(
                    texture.crop(
                        (
                            obj.m_Rect.x,
                            texture.height - obj.m_Rect.y - obj.m_Rect.height,
                            obj.m_Rect.x + obj.m_Rect.width,
                            texture.height - obj.m_Rect.y,
                        )
                    )
                )
                for obj in objs
            ]
        else:
            texture = self.resize(assets[0].read().image)
            self.assets = [texture]

        if self.tint is not None:
            self.assets = [
                ImageChops.multiply(img.convert('RGBA'), Image.new('RGBA', img.size, (*self.tint, 255)))
                for img in self.assets
            ]

    def resize(self, img: Image.Image) -> Image.Image:
        return img.resize((int(img.width * 0.5), int(img.height * 0.5)))

    def anchor_offset(self, background: Image.Image, height: int | None = None) -> float:
        if height is None:
            height = self.assets[0].height
        if self.anchor == AnchorType.TOP:
            return 0
        elif self.anchor == AnchorType.BOTTOM:
            return background.height - height
        elif self.anchor == AnchorType.CENTER:
            return (background.height - height) // 2
        raise Exception(f'Unknown anchor type {self.anchor}')

    def to_clip(self, duration: float) -> VideoClip:
        if len(self.assets) == 1:
            clip = ImageClip(np.array(self.assets[0]))
        else:
            np_images = [np.array(img) for img in self.assets]
            fps = len(np_images) / self.duration
            clip = ImageSequenceClip(np_images, fps=fps)
            # keep displaying the last frame if it ends before the other part
            if clip.duration < duration:  # ty:ignore[unsupported-operator]
                last_frame = ImageClip(np_images[-1]).with_duration(duration - clip.duration)  # ty:ignore[unsupported-operator]
                clip = concatenate_videoclips([clip, last_frame])

        return clip.with_start(self.start)

    @staticmethod
    def get_part(o: OrnamentInfo, part: PartName, container: BetterContainer) -> PartElement:
        if part == PartName.BACKGROUND:
            element = PartElement(part, o.m_backgroundPath)
        elif part == PartName.TOP:
            element = PartElement(part, o.m_topElementPath, o.m_topElementPosition, o.m_animationDuration.y,
                               o.m_animationStartDelay.y)  # fmt: off
        elif part == PartName.BOTTOM:
            element = PartElement(part, o.m_bottomElementPath, o.m_bottomElementPosition, o.m_animationDuration.w,
                               o.m_animationStartDelay.w)  # fmt: off
        elif part == PartName.LEFT:
            element = PartElement(part, o.m_leftElementPath, o.m_leftElementPosition, o.m_animationDuration.x,
                               o.m_animationStartDelay.x, o.m_leftElementAnchor)  # fmt: off
        elif part == PartName.RIGHT:
            element = PartElement(part, o.m_rightElementPath, o.m_rightElementPosition, o.m_animationDuration.z,
                               o.m_animationStartDelay.z, o.m_rightElementAnchor)  # fmt: off
        element._load_asset(o.m_isAnimated, container)
        return element

    @staticmethod
    def get_colorable_parts(
        o: OrnamentInfo, part: PartName, container: BetterContainer, colors: dict[int, tuple[int, int, int]]
    ) -> tuple[list[PartElement], list[PartElement]]:
        colorable = {
            PartName.TOP: o.m_topColorable,
            PartName.BOTTOM: o.m_bottomColorable,
            PartName.LEFT: o.m_leftColorable,
            PartName.RIGHT: o.m_rightColorable,
        }.get(part)
        backs: list[PartElement] = []
        fronts: list[PartElement] = []
        if colorable is None:
            return backs, fronts
        for data in colorable.colorableElementData:
            if (color := colors.get(data.colorSource)) is None:
                continue
            for path, position, back, dest in (
                (data.backElementPath, data.backElementPosition, True, backs),
                (data.frontElementPath, data.frontElementPosition, False, fronts),
            ):
                if not path:
                    continue
                element = PartElement(part, path, position, anchor=data.elementAnchor, colorable_back=back, tint=color)
                try:
                    element._load_asset(0, container)
                except FileNotFoundError:
                    continue
                dest.append(element)
        return backs, fronts

    @staticmethod
    def get_parts_element(
        data: OrnamentInfo, container: BetterContainer, colors: dict[int, tuple[int, int, int]] | None = None
    ) -> list[PartElement]:
        result = []
        for i in PartName:
            try:
                part = PartElement.get_part(data, i, container)
            except FileNotFoundError:
                if i == PartName.BACKGROUND:
                    raise
                continue
            if colors and not data.m_isAnimated and i != PartName.BACKGROUND:
                backs, fronts = PartElement.get_colorable_parts(data, i, container, colors)
                result.extend(backs)
                result.append(part)
                result.extend(fronts)
            else:
                result.append(part)
        return result

    @staticmethod
    def compute_bboxes(parts: list[PartElement]) -> list[Bbox]:
        if (background := next((i for i in parts if i.part_name == PartName.BACKGROUND), None)) is None:
            raise Exception("Can't compute bboxes, No background part")
        background_img = background.assets[0]
        mains = {p.part_name: p.assets[0] for p in parts if p.colorable_back is None}
        bboxes = []
        for part in parts:
            img = part.assets[0]
            if part.colorable_back is not None:
                x, y = PartElement.compute_colorable_position(part, mains[part.part_name], background_img)
            elif part.part_name == PartName.BACKGROUND:
                x, y = 0, 0
            elif part.position is None:
                continue
            elif part.part_name == PartName.TOP:
                x = (background_img.width - img.width) / 2 + part.position.x
                y = 4 - part.position.w - img.height
            elif part.part_name == PartName.BOTTOM:
                x = (background_img.width - img.width) / 2 + part.position.x
                y = background_img.height - part.position.w - 8
            elif part.part_name == PartName.LEFT:
                x = part.position.x - img.width + 8
                y = part.anchor_offset(background_img) - part.position.w
            elif part.part_name == PartName.RIGHT:
                x = background_img.width - part.position.z - 8
                y = part.anchor_offset(background_img) + part.position.y
            x, y = int(x), int(y)
            bboxes.append(Bbox(x, y, img.width, img.height))
        return bboxes

    @staticmethod
    def compute_colorable_position(part: PartElement, main: Image.Image, background: Image.Image) -> tuple[float, float]:
        assert part.position is not None
        back = part.colorable_back
        if part.part_name == PartName.TOP:
            x = (background.width - main.width) / 2 + part.position.x
            y = 4 + (main.height if back else 0) + part.position.y
        elif part.part_name == PartName.BOTTOM:
            x = (background.width - main.width) / 2 + part.position.x
            y = background.height - 8 - (0 if back else main.height) + part.position.y
        elif part.part_name == PartName.LEFT:
            x = 8 + part.position.x
            y = part.anchor_offset(background, main.height) + (main.height if back else 0) + part.position.y
        elif part.part_name == PartName.RIGHT:
            x = background.width - 8 - (0 if back else main.width) + part.position.x
            y = part.anchor_offset(background, main.height) + part.position.y
        else:
            raise Exception(f'Unexpected colorable part {part.part_name}')
        return x, y


class Ornament:
    """
    render dofus ornaments
    """

    pattern_data: ClassVar[Pattern] = re.compile(r'Assets/Content/Ornaments/Data/ornament_(\d+)\.asset')
    pattern_wings: ClassVar[Pattern] = re.compile(r'Assets/Content/Ornaments/Textures/Wings/(WingsTop|WingsBot)_(\d+)\.png')
    WINGS_SCALE: ClassVar[float] = 0.6
    WINGS_CONTENT_MIN_WIDTH: ClassVar[int] = 160
    WINGS_CONTENT_MIN_HEIGHT: ClassVar[int] = 32

    def __init__(self, game_path: Path) -> None:
        aa = get_data_path(game_path, TypeData.aa)
        picto_ui = get_data_path(game_path, TypeData.Picto_UI)

        if (aa_ornament := next(aa.rglob('Standalone*/ornaments_assets_all.bundle'), None)) is None:
            raise FileNotFoundError('ornaments_assets_all.bundle not found')
        self.aa_ornament = str(aa_ornament)
        ornement_asset = str(picto_ui / 'ornament_assets_all.bundle')
        self.env = UnityPy.load(self.aa_ornament, ornement_asset)
        self.container = BetterContainer(self.env)

    @cached_property
    def data(self) -> dict[int, OrnamentInfo]:
        return {
            int(match.group(1)): obj.read()
            for key, obj in self.env.files[self.aa_ornament].container.items()  # ty:ignore[unresolved-attribute]
            if (match := self.pattern_data.fullmatch(key))
        }

    @cached_property
    def wings_pivot_data(self) -> dict[int, dict[str, WingPart]]:
        result: defaultdict[int,  dict[str, WingPart]] = defaultdict(dict)
        for key, obj in self.env.files[self.aa_ornament].container.items():  # ty:ignore[unresolved-attribute]
            if obj.type != ClassIDType.Sprite or not(match:= self.pattern_wings.fullmatch(key)):
                continue
            obj_ = obj.read_typetree()
            result[int(match.group(2))][match.group(1)] = {"w": obj_['m_Rect']['width'], "h": obj_['m_Rect']['height'], "pivot":obj_['m_Pivot']}
        return result

    def save_wings_pivot(self, output :Path):
        file_path = output/ TypeData.aa / "Assets/Content/Ornaments/Data/wing.json"
        file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.write_bytes(orjson.dumps(self.wings_pivot_data, option=orjson.OPT_NON_STR_KEYS))

    def _load_wing_image(self, name: str) -> Image.Image | None:
        key = f'Assets/Content/Ornaments/Textures/Wings/{name}.png'
        sprites = self.container.get_asset_type(key, ClassIDType.Sprite)
        if not sprites:
            return None
        return sprites[0].read().image

    def render_wings(self, index: int) -> Image.Image:
        scale = self.WINGS_SCALE
        content_w = self.WINGS_CONTENT_MIN_WIDTH
        content_h = self.WINGS_CONTENT_MIN_HEIGHT

        meta = self.wings_pivot_data.get(index)
        if not meta or 'WingsTop' not in meta or (top_img := self._load_wing_image(f'WingsTop_{index}')) is None:
            raise FileNotFoundError(f'WingsTop_{index} not found')

        top = meta['WingsTop']
        tw, th = int(top['w'] * scale), int(top['h'] * scale)
        top_img = top_img.resize((tw, th))
        top_y = top['pivot']['y'] * th

        bot = meta.get('WingsBot')
        bot_img = self._load_wing_image(f'WingsBot_{index}') if bot else None
        if bot is not None and bot_img is not None:
            bw, bh = int(bot['w'] * scale), int(bot['h'] * scale)
            bot_img = bot_img.resize((bw, bh))
        else:
            bot_img = None
            bw, bh = 0,0

        canvas_w = max(tw, bw, content_w)
        cx = canvas_w / 2

        placements: list[tuple[Image.Image, Bbox]] = [(top_img, Bbox(int(cx - tw / 2), int(top_y), tw, th))]
        if bot_img is not None and bot is not None:
            bot_y = th + content_h - (1 - bot['pivot']['y']) * bh
            placements.append((bot_img, Bbox(int(cx - bw / 2), int(bot_y), bw, bh)))

        max_bbox = Bbox.compute_max_bbox([b for _, b in placements])
        canvas = Image.new('RGBA', (max_bbox.w, max_bbox.h), (0, 0, 0, 0))
        for img, bbox in placements:
            canvas.paste(img, (bbox.x - max_bbox.x, bbox.y - max_bbox.y), img)
        return canvas

    def save_all_wings(self, output:Path):
        out_folder = output / TypeDataOther.Ornament / 'wings'
        out_folder.mkdir(exist_ok=True, parents=True)
        for i in self.wings_pivot_data.keys():
            img = self.render_wings(i)
            img.save(out_folder / f'{i}.png')


    def save_all(
        self,
        output: Path | str,
        skip_webm: bool = False,
        colors: dict[int, tuple[int, int, int]] | None = None,
    ) -> None:
        """`colors` tints the colorable elements per ColorSource; pass {} to skip them (default colors if None)."""
        if colors is None:
            colors = DEFAULT_COLORS
        if isinstance(output, str):
            output = Path(output)
        output.mkdir(exist_ok=True, parents=True)
        for ornament_id, ornament_data in tqdm(self.data.items(), desc='generate ornaments'):
            try:
                parts = PartElement.get_parts_element(ornament_data, self.container, colors)
                bboxes = PartElement.compute_bboxes(parts)
                max_bbox = Bbox.compute_max_bbox(bboxes)
            except FileNotFoundError as e:
                tqdm.write(f'Error processing {ornament_id}: {e}')
                continue
            if ornament_data.m_isAnimated and not skip_webm:
                max_duration = self.get_duration(ornament_data)
                video = self.generate_animated(parts, bboxes, max_bbox, max_duration)
                video.write_videofile(
                    output / f'{ornament_id}.webm',
                    codec='libvpx',
                    ffmpeg_params=['-pix_fmt', 'yuva420p', '-an', '-vsync', '0'],
                    audio=False,
                    logger=None,
                )
            img = self.generate(parts, bboxes, max_bbox)
            img.save(output / f'{ornament_id}.png')

    def save_sheets(self, output: Path | str) -> None:
        prefix = 'Assets/Content/Ornaments/Textures/Animated/'
        output = (Path(output) / TypeData.aa / prefix).parent
        by_container: dict[str, list] = defaultdict(list)
        for key, obj in self.env.container.items():
            if obj.type == ClassIDType.Sprite and key.startswith(prefix):
                by_container[key].append(obj)
        meta: dict[str, dict] = {}
        for key, objs in by_container.items():
            if len(objs) < 2:
                continue
            sprites = [o.read() for o in objs]
            sprites.sort(key=lambda s: int(s.m_Name.split('_')[-1]))
            sheet: Image.Image = sprites[0].m_RD.texture.read().image
            stem = key.removeprefix(prefix).removesuffix('.png')
            dest = output / 'Sheets' / f'{stem}.png'
            dest.parent.mkdir(exist_ok=True, parents=True)
            sheet.save(dest)
            rect = sprites[0].m_Rect
            meta[stem] = {
                'sheet': [sheet.width, sheet.height],
                'frame': [rect.width, rect.height],
                'frames': [[s.m_Rect.x, sheet.height - s.m_Rect.y - s.m_Rect.height] for s in sprites],
            }
        (output / 'animated.json').write_bytes(orjson.dumps(meta))

    def save_borders(self, output: Path | str) -> None:
        prefix = 'Assets/Content/Ornaments/Textures/'
        borders= {}
        for key, obj in self.env.container.items():
            if obj.type != ClassIDType.Sprite or not key.startswith(prefix):
                continue
            border = obj.read().m_Border
            borders[key.removeprefix(prefix).removesuffix('.png')] = (border.w, border.z, border.y, border.x)
        output = Path(output) / TypeData.aa / prefix
        output.parent.mkdir(exist_ok=True, parents=True)
        (output/'borders.json').write_bytes(orjson.dumps(borders))

    @staticmethod
    def generate_animated(parts: list[PartElement], bboxes: list[Bbox], max_bbox: Bbox, duration: float) -> VideoClip:
        clips = []
        for part, bbox in zip(parts, bboxes):
            clips.append(part.to_clip(duration).with_position((bbox.x - max_bbox.x, bbox.y - max_bbox.y)))
        return CompositeVideoClip(clips, size=(max_bbox.w, max_bbox.h)).with_duration(duration)

    @staticmethod
    def generate(parts: list[PartElement], bboxes: list[Bbox], max_bbox: Bbox) -> Image.Image:
        canvas = Image.new('RGBA', (max_bbox.w, max_bbox.h), (0, 0, 0, 0))
        for part, bbox in zip(parts, bboxes):
            img = part.assets[-1]
            canvas.paste(img, (bbox.x - max_bbox.x, bbox.y - max_bbox.y), img)
        return canvas

    @staticmethod
    def get_duration(data: OrnamentInfo) -> float:
        return max(getattr(data.m_animationDuration, i) + getattr(data.m_animationStartDelay, i) for i in 'xyzw')

    def full_process(self, output: Path | str) -> None:
        output = Path(output)
        output.mkdir(exist_ok=True, parents=True)
        self.save_all(output/ TypeDataOther.Ornament)
        self.save_sheets(output)
        self.save_borders(output)
        self.save_all_wings(output)
        self.save_wings_pivot(output)
