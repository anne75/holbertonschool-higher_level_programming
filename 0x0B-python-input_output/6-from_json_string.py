#!/usr/bin/python3
import json
"""
This is module 6-from_json_string.
This module contains one function
"""


def from_json_string(my_str):
    """
    converts a json representation to a python object

    Arguments:
        my_str: a string

    Return:
        a python object - no error checking
    """
    return json.loads(my_str)
