def arg_parse(args: list) -> int:

    flags: tuple = (
        "-g",
        "-h", "--help",
        "-v", "--version"
    )

    # if no flags
    if len(args) == 1:
        return 0

    # if flag is -g
    elif args[1] in flags[0:1]:

        # if flags is incorrect
        if len(args) < 4:
            return 4

        else:
            return 1

    # if flag is -h, --help
    elif args[1] in flags[1:3]:
        return 2

    # if flag is -v, --version
    elif args[1] in flags[3:5]:
        return 3

    # in else cases
    else:
        return 0
