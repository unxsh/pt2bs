def write_to_file(file: str, main_file: str, ofile: str):

    build_py: str = file % (main_file, ofile)

    with open("build.py", "w") as f:
        f.write(build_py)
