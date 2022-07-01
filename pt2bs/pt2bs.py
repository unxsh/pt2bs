from sys import argv
from args import arg_parse


def main() -> None:

    arg_num: int = arg_parse(argv)  # get arg number

    print(arg_num)  # log

    # if flag is -g, --generate
    if arg_num == 1:
        pass

    # if flag is -h, --help
    elif arg_num == 2:
        pass

    # if flag is -v, --version
    elif arg_num == 3:
        pass

    # in else cases
    else:
        pass


if __name__ == "__main__":
    main()
