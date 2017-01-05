#!/usr/bin/python3
import sys

if __name__ == "__main__":
    li = sys.argv[1:]
    size = len(li)
    print("{:d} argument{}{}".format(size, "" if size <= 1 else "s",
          "." if not size else ":"))
    for index, arg in enumerate(li):
        print("{:d}: {}".format(index + 1, arg))
