import argparse

def get_parser() -> argparse.ArgumentParser: ...
def extract_subcommand(args: str) -> tuple[str | None, str | None]: ...
def main_or_fail() -> None: ...
