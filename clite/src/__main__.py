import argparse
import os
import sys
from tap import Tap
from clite.src.command import import_command
from clite.src.commands.commands import available_commands
from clite.src.errors import CliteExecError


class Parser(Tap):
    pass


def extract_subcommand(args):
    if len(args) > 1:
        return(args[0], args[1], args[2:])
    else:
        return(args[0], None, None)


def main_or_fail():
    program_name, subcommand_name, subcommand_args = extract_subcommand(sys.argv)
    if subcommand_name:
        subcommand = import_command(subcommand_name)
        if subcommand:
            sys.argv[0] = f"{sys.argv[0]} {subcommand_name}"

            try:
                sys.exit(subcommand.run(*subcommand_args))
            except CliteExecError as e:
                print(f"error: {e.__class__.__name__}({e})", file=sys.stderr)
        else:
            print("error: unknown command\n")
            print(available_commands())
            sys.exit(1)
    else:
        short_program = os.path.split(program_name)[-1]

        Parser(formatter_class=argparse.RawDescriptionHelpFormatter, usage=f"{short_program} [command]", epilog=available_commands()).print_help()


if __name__ == "__main__":
    main_or_fail()
