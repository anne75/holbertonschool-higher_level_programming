#!/usr/bin/python3
"""
This is module 3-write_file
This module contains one function
"""


def write_file(filename="", text=""):
    """
    write a string to a file

    Arguments:
        filename: path to file
        text: a string
    """
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
