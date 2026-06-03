import subprocess
import warnings
from pathlib import Path

import orjson
import UnityPy
from tqdm import tqdm
from UnityPy import Environment
from UnityPy.config import UnityVersionFallbackWarning

from pydofus3.enum_data import TypeData, TypeDataOther, get_data_path
from pydofus3.tools import get_unity_version


def extract_audio(files: list[Path], output: Path) -> None:
    """
    extract audio from dofus bank file
    """
    if not files:
        return
    bin = Path(__file__).parent / 'salt/Salt.Convert.dll'
    output.mkdir(exist_ok=True, parents=True)
    temp = output/ 'temp.json'
    master_bank = files[0].parent / 'Master.bank'
    temp.write_bytes(orjson.dumps(list(map(str, files))))
    subprocess.run(['dotnet', bin, master_bank, temp, output])
    temp.unlink()

def process_audio_manager(output:Path, dofus_path:Path)->None:
    warnings.simplefilter('ignore', UnityVersionFallbackWarning)
    UnityPy.config.FALLBACK_UNITY_VERSION =  get_unity_version(dofus_path)
    aa_dir = next(iter(get_data_path(dofus_path,  TypeData.aa).glob('**/gameassets_assets_all.bundle')), None)
    if aa_dir is None:
        raise FileNotFoundError("gameassets_assets_all.bundle")
    env: Environment = UnityPy.load(str(aa_dir))
    audio_lib = env.container['Assets/Configuration/Audio/AudioManagerLibrary.asset'].read_typetree()
    audio_folder = output / TypeDataOther.Audio
    mtimes = {str(p.parent.relative_to(audio_folder)): int(p.stat().st_mtime) for p in audio_folder.rglob("info.json")}
    result = dict()
    for i in tqdm(audio_lib['m_eventInfoSet']['m_entries'], desc='process audio manager'):
        event_path = i['path'].removeprefix('event:/')
        time = mtimes.get(event_path, 0)
        result[i['guid']] = [event_path, time]
    output_file = output / TypeDataOther.Audio/'audio_manager.json'
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_bytes(orjson.dumps(result))
