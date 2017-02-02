#!/usr/bin/python3
"""
This is module 4-append_write
This module contains one function
"""


def append_write(filename="", text=""):
    """
    append a string to a file

    Arguments:
        filename: apth to file
        text: a string

    Return:
        number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
    return count
