#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    if len == 1:
        print("{}".format(len - 1), "arguments.")
    else:
        print("{}".format(len - 1), "arguments:")
        for i in range(1, len):
            print("{}:".format(i), "{}".format(sys.argv[i]))
