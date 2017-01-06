#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    d = {"+": add, "-": sub, "*": mul, "/": div}
    for op in "+-*/":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, d[op](a, b)))
