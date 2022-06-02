#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    if ln == 1:
        print('0 arguments.')
    else:
        print('{:d} arguments:'.format(ln - 1))
        for i in range(1, ln):
            print('{:d}: {:s}'.format(i, argv[i]))

    
