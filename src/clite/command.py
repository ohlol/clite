import importlib.util
import os
import sys


def import_command(cmd):
    try:
        spec_path = os.path.join(os.path.dirname(__file__), "commands", f"{cmd}.py")
        spec = importlib.util.spec_from_file_location(f"clite.commands.{cmd}", spec_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["module.name"] = mod
        spec.loader.exec_module(mod)
        return(mod)
    except FileNotFoundError:
        return(None)
