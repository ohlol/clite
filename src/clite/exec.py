import subprocess
from typing import Any


def run(
    *cmd: str, merge_outputs: bool = False, run_kwargs: dict[Any, Any]
) -> subprocess.CompletedProcess[bytes]:
    run_kwargs["check"] = True

    if merge_outputs:
        run_kwargs["capture_output"] = True

    return subprocess.run(cmd, **run_kwargs)
