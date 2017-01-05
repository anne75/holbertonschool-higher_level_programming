#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main(a, b, operator):
    """ Main function

    Args:
        a: first integer
        b: second integer
        operator: operator
    """
    d = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in d:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, d[operator](a, b)))


if __name__ == "__main__":
    if not len(sys.argv[1:]) == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # I should use try statement for int ?
    main(int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])
