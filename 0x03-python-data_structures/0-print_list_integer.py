#!/usr/bin/python3


def print_list_integer(mylist=[]):
    """
    print the elements of a list of int
    """
    if mylist:
        print("\n".join(["{:d}".format(element) for element in mylist]))
