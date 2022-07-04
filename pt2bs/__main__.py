from gc import disable as disable_gc  # disable gc
from sys import argv  # command line args

from argp import arg_parse
from perform import arg_0, arg_1, arg_2, arg_3, arg_4


def main() -> None:

    disable_gc()  # disable garbage collector

    arg_num: int = arg_parse(argv)  # get arg number

    # if flag is -g
    if arg_num == 1:
        arg_mode: int = int(argv[2])
        arg_1(arg_mode, argv[3], argv[4])

    # if flag is -h, --help
    elif arg_num == 2:
        arg_2()

    # if flag is -v, --version
    elif arg_num == 3:
        arg_3()

    # if flags is incorrect
    elif arg_num == 4:
        arg_4()

    # in else cases
    else:
        arg_0()


if __name__ == "__main__":
    main()
