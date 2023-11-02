#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for x in range(argc):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
