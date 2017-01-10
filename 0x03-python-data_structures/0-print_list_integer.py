#!/usr/bin/python3


def print_list_integer(mylist=[]):
    """
    print the elements of a list of int
    """
    if (mylist and mylist != None):
        print("\n".join("{:d}".format(x) for x in mylist))
