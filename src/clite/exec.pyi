import subprocess
from typing import Any

def run(
    *cmd: str, merge_outputs: bool = ..., run_kwargs: dict[Any, Any]
) -> subprocess.CompletedProcess[bytes]: ...
