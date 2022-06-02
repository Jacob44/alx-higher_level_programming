#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    from sys import argv
    ln = len(argv)
    a = argv[1]
    op = argv[2]
    b = argv[3]
    if ln != 4:
        print('{:s}'.format('Usage: ./100-my_calculator.py <a> <operator> <b>'))
        exit(1)
    else:
        if op == '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif op == '-':
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        if op == '*':
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        if op == '/':
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
        else:
            print('{:s}'.format('Unknown operator. Available operators: +, -, * and /'))
            exit(1)
  
