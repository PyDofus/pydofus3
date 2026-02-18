import re
import subprocess
from pathlib import Path
from proto_schema_parser.parser import Parser
from proto_schema_parser.generator import Generator
from proto_schema_parser.ast import Import, Message, OneOf, File

content_regex = re.compile(r'(google\.protobuf\.Any )\w+( =)')

def protodec(dummy_dll_path: Path, output_dir: Path = Path('output')):
    """
    extract obfu proto with protodec
    """
    protodec_path = Path(__file__).parent / 'protodec/protodec.dll'
    for f in dummy_dll_path.rglob('Ankama.Dofus.Protocol.*.dll'):
        name = f.stem.split('.')[-1]
        subprocess.run(['dotnet', protodec_path, f, output_dir / f'{name}.proto'])
    if (game_proto:= (output_dir / 'Game.proto')).is_file():
        proto = Parser().parse(game_proto.read_text())
        proto.file_elements.insert(1, Import("google/protobuf/any.proto"))
        edit_base_msg(proto)
        proto_text = Generator().generate(proto)
        proto_text = re.sub(content_regex, r'\1content\2', proto_text)
        game_proto.write_text(proto_text)
    if (game_proto:= (output_dir / 'Connection.proto')).is_file():
        proto = Parser().parse(game_proto.read_text())
        edit_base_msg(proto, True)
        game_proto.write_text(Generator().generate(proto))


def edit_base_msg(proto:File, is_login:bool=False) -> None:
    for elem in proto.file_elements:
        if isinstance(elem, Message):
            for f in elem.elements:
                if isinstance(f, OneOf):
                    elem.name = "LoginMessage" if is_login else "Message"
                    f.name = "content"
                    return
