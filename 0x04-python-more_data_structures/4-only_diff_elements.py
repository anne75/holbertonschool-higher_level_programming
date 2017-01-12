#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    return the set of elements contained in set_1 or set_2
    but not their intersection

    set_1: a set
    set_2: a set

    Return: a set
    """
    return (set_1 ^ set_2)
