#!/usr/bin/python3
print(", ".join(["{:d}{:d}".format(x, y) for x in range(10)
                for y in range(x + 1, 10)]))
