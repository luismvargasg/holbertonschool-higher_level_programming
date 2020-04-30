#!/usr/bin/python
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    i = 1
    res = 0
    while i <= argc:
        res += int(sys.argv[i])
        i += 1
    print("{:d}".format(res))
