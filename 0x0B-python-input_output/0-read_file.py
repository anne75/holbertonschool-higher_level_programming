#!/usr/bin/python3
"""
This is module 0-read_file.
This module contains only one function.
"""


def read_file(filename=""):
    """
    reads and prints a file

    Arguments:
        filename: path to file, may or not be valid

    for error handling
    http://stackoverflow.com/questions/713794/
    catching-an-exception-while-using-a-python-with-statement
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
