import argparse
import sys

from clite.command import import_command
from clite.commands.commands import available_commands
from clite.errors import CliteExecError
from clite.util.version import __version__


def get_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage="%(prog)s [command]",
        epilog=available_commands(),
    )
    parser.add_argument(
        "-V",
        action="version",
        help="print version",
        version="%(prog)s {version}".format(version=__version__),
    )

    return parser


def extract_subcommand(args):
    if len(args) > 1:
        return (args[1], args[2:])
    else:
        return (None, None)


def main_or_fail():
    subcommand_name, subcommand_args = extract_subcommand(sys.argv)

    parser = get_parser()
    parser.parse_known_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    if subcommand_name:
        subcommand = import_command(subcommand_name)
        if subcommand:
            sys.argv[0] = f"{sys.argv[0]} {subcommand_name}"

            try:
                sys.exit(subcommand.run(*subcommand_args))
            except CliteExecError as e:
                print(f"error: {e.__class__.__name__}({e})", file=sys.stderr)
                sys.exit(1)
        else:
            print("error: unknown command\n")
            print(available_commands())
            sys.exit(1)


if __name__ == "__main__":
    main_or_fail()
