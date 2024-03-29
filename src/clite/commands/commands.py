import argparse
from importlib.resources import files
from pathlib import Path
from typing import Generator


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    return parser


def all_commands() -> Generator[str, None, None]:
    paths = [str(f) for f in files("clite.commands").iterdir()]
    for f in sorted(paths):
        p = Path(f)
        if p.suffix == ".py":
            yield p.stem


def available_commands() -> str:
    commands_str = "\n".join([cmd for cmd in all_commands()])

    return f"""available commands:

{commands_str}"""


def run(*args: str) -> int:
    parser = get_parser()
    parser.parse_args(args=args)

    print(available_commands())

    return 0
