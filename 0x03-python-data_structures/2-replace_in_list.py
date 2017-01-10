#!/usr/bin/python


def replace_in_list(mylist, idx, element):
    """
    replaces an element of a list at index
    if idx is out of range do not modify the list

    DO NOT use try/except
    """
    size = len(mylist)
    if (-size <= idx < size):
        mylist[idx] = element
    return (mylist)
