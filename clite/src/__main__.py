import sys
from tap import Tap
from clite.src.command import import_command


class Parser(Tap):
    pass


def extract_subcommand(args):
    if len(args) > 1:
        return args[1], args[2:]
    else:
        return None, None


def main():
    subcommand_name, subcommand_args = extract_subcommand(sys.argv)
    if subcommand_name:
        subcommand = import_command(subcommand_name)
        if subcommand:
            sys.argv[0] = f"{sys.argv[0]} {subcommand_name}"
            subcommand.run(*subcommand_args)
        else:
            args = Parser().parse_args()


if __name__ == "__main__":
    main()
