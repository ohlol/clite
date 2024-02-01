from tap import Tap
import importlib.resources


class Parser(Tap):
    pass


def all_commands():
    for f in sorted(importlib.resources.files("clite.src.commands").iterdir()):
        if f.suffix == ".py":
            yield f.stem

def run(*args):
    Parser().parse_args(args)
    print(*[cmd for cmd in all_commands()], sep="\n")
