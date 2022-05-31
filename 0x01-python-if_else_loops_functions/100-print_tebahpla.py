#!/usr/bin/python3
for k in reversed(range(ord('a'), ord('z') + 1)):
    if (k % 2 == 0):
        print('{:s}'.format(chr(k)), end='')
    else:
        k = k - 32
        print('{:s}'.format(chr(k)), end='')
