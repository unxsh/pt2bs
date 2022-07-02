from gc import disable as disable_gc
from sys import argv

from args import arg_parse
from perform import arg_0, arg_1, arg_2, arg_3


def main() -> None:

    disable_gc()  # disable garbage collector

    arg_num: int = arg_parse(argv)  # get arg number

    # if flag is -g, --generate
    if arg_num == 1:
        if len(argv) < 4:
            print("flags is incorrect")

        else:
            arg_1(argv[2], argv[3])

    # if flag is -h, --help
    elif arg_num == 2:
        arg_2()

    # if flag is -v, --version
    elif arg_num == 3:
        arg_3()

    # in else cases
    else:
        arg_0()


if __name__ == "__main__":
    main()
