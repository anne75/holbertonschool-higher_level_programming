#!/usr/bin/python


def replace_in_list(mylist, idx, element):
    if mylist:
        size = len(mylist)
        if (0 <= idx < size):
            mylist[idx] = element
    return (mylist)
