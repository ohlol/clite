import subprocess

from clite.errors import CliteExecError


def run(*cmd, merge_outputs=False, **run_kwargs):
    run_kwargs["check"] = True

    if merge_outputs:
        run_kwargs["capture_output"] = True

    try:
        return subprocess.run(cmd, **run_kwargs)
    except subprocess.CalledProcessError:
        raise CliteExecError(*cmd)
