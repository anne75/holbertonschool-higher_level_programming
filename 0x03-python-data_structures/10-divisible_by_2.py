#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    return a list stating if each element in my_list is even (True)
    or odd (False)
    """
    return ([True if x % 2 == 0 else False for x in my_list])
