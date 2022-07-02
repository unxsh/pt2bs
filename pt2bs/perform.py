from os import _exit as fexit  # import for fast exit

from assets import (build_py, cmassage, empty_field, helpmsg, io_error,
                    main_file, o_file, programmsg, version)
from funcs import write_to_file


def arg_1(main_file: str, ofile: str) -> None:
    try:
        write_to_file(build_py, main_file, ofile)
        print(cmassage)
    except IOError:
        print(io_error)


def arg_2() -> None:

    print(programmsg)
    print(helpmsg)

    fexit(0)  # fast exit


def arg_3() -> None:

    print(version)  # print program version from assets
    fexit(0)  # fast exit


def arg_0() -> None:
    print(main_file)  # message
    mainf: str = input(":")

    print(o_file)  # message
    ofile: str = input(":")

    if mainf == "" or ofile == "":
        print(empty_field)

    else:
        try:
            write_to_file(build_py, mainf, ofile)
            print(cmassage)
        except IOError:
            print(io_error)