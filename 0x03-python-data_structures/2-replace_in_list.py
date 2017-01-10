#!/usr/bin/python


def replace_in_list(mylist, idx, element):
    """
    replaces an element of a list at index
    if idx is out of range do not modify the list

    DO NOT use try/except
    DO NOT consider negative indexes
    """
    size = len(mylist)
    if (0 <= idx < size):
        mylist[idx] = element
    return (mylist)
