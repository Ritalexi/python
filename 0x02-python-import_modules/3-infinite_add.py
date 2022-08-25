#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    k = 0
    for i in range(1, len):
        j = int(sys.argv[i])
        k += j
    print("{}".format(k))
