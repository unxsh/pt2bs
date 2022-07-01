from gc import disable as disable_gc
from os import _exit as fexit  # import for fast exit
from sys import argv

from args import arg_parse
from assets import helpmsg, programmsg


def main() -> None:

    disable_gc()  # disable garbage collector

    arg_num: int = arg_parse(argv)  # get arg number

    # if flag is -g, --generate
    if arg_num == 1:
        pass

    # if flag is -h, --help
    elif arg_num == 2:
        print(programmsg)
        print(helpmsg)

        fexit(0)  # fast exit

    # if flag is -v, --version
    elif arg_num == 3:
        pass

    # in else cases
    else:
        pass


if __name__ == "__main__":
    main()
