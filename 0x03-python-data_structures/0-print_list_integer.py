#!/usr/bin/python3


def print_list_integer(mylist=[]):
    """
    print the elements of a list of int
    """
    print("\n".join("{:d}".format(x) for x in mylist))
