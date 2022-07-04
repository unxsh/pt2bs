from os import system as sh


def write_to_file(file: str, main_file: str, ofile: str) -> None:

    build_py: str = file % (main_file, ofile)

    with open("build.py", "w") as f:
        f.write(build_py)


def make_exec() -> None:
    sh("chmod +x build.py")
