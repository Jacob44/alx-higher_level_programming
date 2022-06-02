#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    sm = 0
    for i in range(1, ln):
        sm += int(argv[i])
    print('{:d}'.format(sm))
