import subprocess
from pathlib import Path

import orjson


def extract_audio(files: list[Path], output: Path) -> None:
    """
    extract audio from dofus bank file
    """
    if not files:
        return
    bin = Path(__file__).parent / 'salt/Salt.Convert.dll'
    temp = Path('temp.json')
    master_bank = files[0].parent / 'Master.bank'
    temp.write_bytes(orjson.dumps(list(map(str, files))))
    subprocess.run(['dotnet', bin, master_bank, temp, output])
    temp.unlink()
