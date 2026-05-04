"""
render dofus ornaments
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import IntEnum, StrEnum
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Pattern

import numpy as np
import UnityPy
from moviepy import CompositeVideoClip, ImageClip, ImageSequenceClip, VideoClip, concatenate_videoclips
from PIL import Image
from tqdm import tqdm
from UnityPy.enums import ClassIDType

from pydofus3.enum_data import TypeData, get_data_path
from pydofus3.extractor.data.tools import BetterContainer

if TYPE_CHECKING:
    from pydofus3.generated.stub.aa_standalonewindows64 import OrnamentInfo, Vector4f


class AnchorType(IntEnum):
    TOP = 0
    CENTER = 1
    BOTTOM = 2


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

    def resize(self, img: Image.Image) -> Image.Image:
        return img.resize((int(img.width * 0.5), int(img.height * 0.5)))

    def anchor_offset(self, background: Image.Image) -> float:
        if self.anchor == AnchorType.TOP:
            return 0
        elif self.anchor == AnchorType.BOTTOM:
            return background.height - self.assets[0].height
        elif self.anchor == AnchorType.CENTER:
            return (background.height - self.assets[0].height) // 2
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
    def get_parts_element(data: OrnamentInfo, container: BetterContainer) -> list[PartElement]:
        result = []
        for i in PartName:
            try:
                part = PartElement.get_part(data, i, container)
            except FileNotFoundError:
                if i == PartName.BACKGROUND:
                    raise
                continue
            result.append(part)
        return result

    @staticmethod
    def compute_bboxes(parts: list[PartElement]) -> list[Bbox]:
        if (background := next((i for i in parts if i.part_name == PartName.BACKGROUND), None)) is None:
            raise Exception("Can't compute bboxes, No background part")
        background_img = background.assets[0]
        bboxes = []
        for part in parts:
            img = part.assets[0]
            if part.part_name == PartName.BACKGROUND:
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


class Ornament:
    """
    render dofus ornaments
    """

    pattern_data: ClassVar[Pattern] = re.compile(r'Assets/Content/Ornaments/Data/ornament_(\d+)\.asset')

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

    def save_all(self, output: Path | str, skip_webm: bool = False) -> None:
        if isinstance(output, str):
            output = Path(output)
        output.mkdir(exist_ok=True, parents=True)
        for ornament_id, ornament_data in tqdm(self.data.items(), desc='generate ornaments'):
            try:
                parts = PartElement.get_parts_element(ornament_data, self.container)
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
