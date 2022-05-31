#!/usr/bin/python3
for l in reversed(range(ord('a'), ord('z') + 1)):
    if (l % 2 == 0):
        print('{:s}'.format(chr(l)), end='')
    else:
        l = l - 32
        print('{:s}'.format(chr(l)), end='')
