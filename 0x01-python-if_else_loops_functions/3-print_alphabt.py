#!/usr/bin/python3
r = ''
for i in range(97, 123):
    s = chr(i)
    r += s
print(r[0:4] + r[5:16] + r[17:], end='')
