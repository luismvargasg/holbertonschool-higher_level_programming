#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    i = 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:\n{:d}: {:s}".format(argc, argc, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        while i <= argc:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
