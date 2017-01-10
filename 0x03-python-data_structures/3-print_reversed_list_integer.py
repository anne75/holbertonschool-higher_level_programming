#!/usr/bin/python3


def print_reversed_list_integer(li=[]):
    """
    print a list of int in reverse order
    """
    if li:
        if li is not None:
            print("\n".join(["{:d}".format(x) for x in reversed(li)]))
