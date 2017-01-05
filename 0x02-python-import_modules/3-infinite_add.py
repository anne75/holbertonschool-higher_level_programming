#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for number in sys.argv[1:]:
        try:
            sum += int(number)
        except ValueError:
            raise SystemExit("Only provide natural numbers")
    print("{:d}".format(sum))


# print("{:d}".format(sum(int(x) for x in sys.argv[1:])))
