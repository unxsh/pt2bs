def arg_parse(args: list) -> int:

    flags: tuple = (
        "-g", "--generate",
        "-h", "--help",
        "-v", "--version"
    )

    # if no flags
    if len(args) == 1:
        return 0

    # if flag is -g
    elif args[1] in flags[0:2]:

        # if flags is incorrect
        if len(args) < 5:
            return 4

        else:
            return 1

    # if flag is -h, --help
    elif args[1] in flags[2:4]:
        return 2

    # if flag is -v, --version
    elif args[1] in flags[4:6]:
        return 3

    # in else cases
    else:
        return 0
