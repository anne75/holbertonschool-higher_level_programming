#!/usr/bin/python3
"""
This is module 1-number_of_lines
This module contains one function
"""


def number_of_lines(filename=""):
    """
    Number of lines in a file

    Arguments:
        filename: path to file

    Return:
        number of lines in file
    """
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
