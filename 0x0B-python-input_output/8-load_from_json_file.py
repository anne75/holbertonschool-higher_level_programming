#!/usr/bin/python3
import json
"""
This is module 8-load_from_json.
This module contains one function.
"""


def load_from_json_file(filename):
    """
    Creates a python object from a text file

    Arguments:
        filename: path to file

    Returns:
       a python object - no error checking
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
