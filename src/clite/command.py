import os
from pydoc import importfile
from types import ModuleType


def import_command(cmd: str) -> ModuleType:
    try:
        return importfile(
            os.path.join(os.path.dirname(__file__), "commands", f"{cmd}.py")
        )
    except FileNotFoundError:
        return None
