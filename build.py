#!/usr/bin/env python3

from os import system as sh
from os import mkdir
from shutil import rmtree
from os import chdir
from sys import argv

# main file in program
MAIN: str = "__main__.py"

# output file
OFILE: str = "program"

# python for python interpreter
PYFLAGS: str = """ \
    -OO \
"""

# compile flags
CFLAGS: str = """ \
    --warn-implicit-exceptions \
    --warn-unusual-code \
    --follow-imports \
    --python-flag=-OO \
    --disable-ccache \
    --lto=yes \
"""

# dir for binary file
BINDIR: str = "/usr/local/bin"

# build command
BUILD: str = f"python {PYFLAGS} -m nuitka {CFLAGS} -o {OFILE} ../{MAIN}"


# if flags in incorrect
if len(argv) == 1:
    print("incorrect flags")

# install option
elif argv[1] == "install":
    try:
        # make build/ dir & change active dir to build/
        mkdir("build/")
        mkdir("build/")
        chdir("build/")

    # if dir already exist
    except FileExistsError:
        rmtree("build/")
        mkdir("build/")
        chdir("build/")

    # execute build command
    sh(BUILD)

    # move OFILE file in BINDIR
    sh(f"sudo mv {OFILE} {BINDIR}")

# build option
elif argv[1] == "build":
    try:
        # make build/ dir & change active dir to build/
        mkdir("build/")
        mkdir("build/")
        chdir("build/")

    # if dir already exist
    except FileExistsError:
        rmtree("build/")
        mkdir("build/")
        chdir("build/")

    # execute build command
    sh(BUILD)

else:
    print("incorrect flags")
