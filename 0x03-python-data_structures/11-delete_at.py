#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    delete an element in a list
    DO NOT use pop, negative indexes
    """
    size = len(my_list)
    if (0 <= idx < size):
        del my_list[idx]
    return (my_list)
