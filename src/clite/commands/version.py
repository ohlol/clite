import argparse

from clite.util.version import __version__


def get_parser():
    parser = argparse.ArgumentParser()

    return parser


def run(*args):
    parser = get_parser()
    parser.parse_args(args=args)

    print(f"version: {__version__}")

    return 0
