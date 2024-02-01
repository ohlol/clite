from tap import Tap

from clite.src import __version__


class Parser(Tap):
    pass


def run(*args):
    Parser().parse_args(args)
    print(f"version: {__version__}")

    return(0)
