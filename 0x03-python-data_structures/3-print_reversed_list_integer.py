#!/usr/bin/python3


def print_reversed_list_integer(li=[]):
    """
    print a list of int in reverse order
    """
    if li is not None:
        for element in reversed(li):
            print("{:d}".format(element))
    return (None)
