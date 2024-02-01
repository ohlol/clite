import argparse
import sys

if sys.version_info >= (3, 10):
    from importlib.resources import files
else:
    from importlib_resources import files


def get_parser():
    parser = argparse.ArgumentParser()

    return parser


def all_commands():
    for f in sorted(files("clite.commands").iterdir()):
        if f.suffix == ".py":
            yield f.stem


def available_commands():
    commands_str = "\n".join([cmd for cmd in all_commands()])

    return f"""available commands:

{commands_str}"""


def run(*args):
    parser = get_parser()
    parser.parse_args(args=args)

    print(available_commands())

    return 0
