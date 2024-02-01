from tap import Tap
import importlib.resources


class Parser(Tap):
    pass


def all_commands():
    for f in sorted(importlib.resources.files("clite.commands").iterdir()):
        if f.suffix == ".py":
            yield f.stem


def available_commands():
    commands_str = "\n".join([cmd for cmd in all_commands()])

    return f"""available commands:

{commands_str}"""


def run(*args):
    Parser().parse_args(args)
    print(available_commands())

    return(0)
