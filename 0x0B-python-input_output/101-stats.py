#!/usr/bin/python3
import sys
import signal
"""
This is module 101-stats
This module parses a log
"""


def print_sorted_dict(d):
    print("\n".join(["{}: {:d}".format(k, d[k])
                     for k in sorted(d.keys())]))


def parse_stdin():
    """parses a formatted stdin"""
    size = 0
    count = 0
    status_codes = {}
    try:
        for line in sys.stdin:
            line_split = line.split()
            try:
                size += int(line_split[-1])
            except TypeError:
                continue
            count += 1
            status_codes[line_split[-2]] = status_codes.get(line_split[-2],
                                                            0) + 1
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
