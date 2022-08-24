#!/usr/bin/python3
r = ''
for i in range(97, 123):
    s = chr(i)
    r += s
print("{}".format(r)[0:4] + "{}".format(r)[5:16] + "{}".format(r)[17:])
