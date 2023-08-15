#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    elif argv_len == 1:
        print("{} argument:".format(argv_len))
    else:
        print("{} arguments:".format(argv_len))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
