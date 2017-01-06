#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    d = {"+": add, "-": sub, "*": mul, "/": div}

    if not len(sys.argv[1:]) == 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in d:
        print("Unknown operator. Only: +, -, * and / available")
        sys.exit(1)
    # I should use try statement for int ?
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {} {:d} = {:d}".format(
        a, sys.argv[2], b, d[sys.argv[2]](a, b)))
