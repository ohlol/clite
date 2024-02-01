from clite.exec import run


def is_m1() -> bool:
    cmd = ["sysctl", "-n", "machdep.cpu.brand_string"]
    result = run(*cmd, merge_outputs=True)
    return("M1" in result.stdout.decode("utf-8"))
