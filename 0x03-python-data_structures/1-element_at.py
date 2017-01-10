#!/usr/bin/python3


def element_at(mylist, idx):
    """
    return the element of the list at index idx
    otherwise return None

    DO NOt use try/except
    """
    if (idx < len(mylist)):
        return (mylist[idx])
    return (None)
