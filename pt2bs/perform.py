from os import _exit as fexit  # import for fast exit

from assets import (args_error, build_py_1, build_py_2, build_py_3, cmassage,
                    empty_field_error, helpmsg, io_error, main_file,
                    mode_error, modes, o_file, version)
from funcs import make_exec, write_to_file


def arg_1(mode: int, main_file: str, ofile: str) -> None:
    """if flag is -g"""

    try:
        if mode == 1:
            write_to_file(build_py_1, main_file, ofile)
            make_exec()  # make file executable

            print(cmassage)
            fexit(0)  # fast exit

        elif mode == 2:
            write_to_file(build_py_2, main_file, ofile)
            make_exec()  # make file executable

            print(cmassage)
            fexit(0)  # fast exit

        elif mode == 3:
            write_to_file(build_py_3, main_file, ofile)
            make_exec()  # make file executable

            print(cmassage)
            fexit(0)  # fast exit

    except IOError:
        print(io_error)
        fexit(1)  # fast exit


def arg_2() -> None:
    """if flag is -h, --help"""

    print(helpmsg)

    fexit(0)  # fast exit


def arg_3() -> None:
    """if flag is -v, --version"""

    print(version)  # print program version from assets
    fexit(0)  # fast exit


def arg_4() -> None:
    """if flags is incorrect"""

    print(args_error)
    fexit(0)


def arg_0() -> None:
    """if no flags"""

    print(modes)  # message
    mode: str = input(":")

    # convert mode type
    if mode == "":
        print(empty_field_error)
        fexit(1)

    else:
        try:
            int_mode: int = int(mode)
            if int_mode > 3 or int_mode < 1:
                print(mode_error)
                fexit(1)

            else:
                print(main_file)  # message
                mainf: str = input(":")

                if mainf == "":
                    print(empty_field_error)
                    fexit(1)

                else:
                    print(o_file)  # message
                    ofile: str = input(":")

                    if ofile == "":
                        print(empty_field_error)
                        fexit(1)

                    else:
                        if mainf == "" or ofile == "" or mode == "":
                            print(empty_field_error)
                            fexit(1)

                        else:
                            try:

                                if int_mode == 1:
                                    write_to_file(build_py_1, mainf, ofile)

                                    make_exec()  # make file executable
                                    print(cmassage)
                                    fexit(0)  # fast exit

                                elif int_mode == 2:
                                    write_to_file(build_py_2, mainf, ofile)

                                    make_exec()  # make file executable
                                    print(cmassage)
                                    fexit(0)  # fast exit

                                elif int_mode == 3:
                                    write_to_file(build_py_3, mainf, ofile)

                                    make_exec()  # make file executable
                                    print(cmassage)
                                    fexit(0)  # fast exit

                            except IOError:
                                print(io_error)
                                fexit(1)  # fast exit

        except ValueError:
            print(mode_error)
            fexit(1)
