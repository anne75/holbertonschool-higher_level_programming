#!/usr/bin/python3
"""
This is module 100-append_after
This module contains one function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text after a triggering pattern

    Arguments:
       filename: path to file
       search_string: pattern to look for
       new_string: line to insert after the pattern is found
    """
    new_content = ""
    with open(filename, mode="r+", encoding="utf-8") as f:
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string
        f.seek(0)
        f.write(new_content)
