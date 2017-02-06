#!/usr/bin/python3
import sys
import signal
import re
"""
This is module 101-stats
This module parses a log
"""


def print_sorted_dict(d):
    if d:
        print("\n".join(["{}: {:d}".format(k, d[k])
                         for k in sorted(d.keys())]))


def parse_stdin():
    """parses a formatted stdin"""
    size = 0
    count = 0
    status_codes = {}
    possibles = ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        for line in sys.stdin:
            line_split = line.split()
            if line_split[-1].isdecimal():
                size += int(line_split[-1])
                if line_split[-2] in possibles:
                    status_codes[line_split[-2]] = status_codes.get(
                        line_split[-2], 0) + 1
            count += 1
            if count % 10 == 0:
                print("File size: {:d}".format(size))
                print_sorted_dict(status_codes)
    except KeyboardInterrupt:
        print("File size: {:d}".format(size))
        print_sorted_dict(status_codes)
        raise
    print("File size: {:d}".format(size))
    print_sorted_dict(status_codes)


parse_stdin()
