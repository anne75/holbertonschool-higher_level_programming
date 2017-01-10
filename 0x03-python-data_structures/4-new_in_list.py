#!/usr/bin/python3


def new_in_list(li, idx, element):
    """
    create a copy of a list, modifying the element
    at idx if idx in the right range

    DO NOT use try/except
    DO NOT consider neagive indexes
    """
    new = li[:]
    size = len(li)
    if (0 <= idx < size):
        new[idx] = element
    return (new)