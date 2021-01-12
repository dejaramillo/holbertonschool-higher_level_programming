#!/usr/bin/python3
count = 122
for i in reversed(range(97, 123)):
    if count > i:
        print("{}".format(chr(i - 32)), end='')
        count -= 2
    else:
        print("{}".format(chr(i)), end='')
