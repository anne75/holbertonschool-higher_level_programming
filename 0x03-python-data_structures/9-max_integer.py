#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    return the maximum value in a list of ints
    DO NOT use max
    """
    if not my_list or my_list is None:
        return None

    max_value = my_list[0]
    for n in my_list:
        if n > max_value:
            max_value = n
    return (max_value)

# RIP reduce
