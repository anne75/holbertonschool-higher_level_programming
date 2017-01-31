#!/usr/bin/python3
"""
This is module 0-lookup.

This module only contains one function.
"""


def lookup(obj):
    """
    Lists all the available attributes and methods of an object hopefully
    dir may not be exhaustive per documentation

    Arguments:
        obj: any object

    Returns:
        a list
    """
    return dir(obj)
