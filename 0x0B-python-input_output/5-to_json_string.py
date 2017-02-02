#!/usr/bin/python3
import json
"""
This is module 5-to_json_string.
This module contains one function.
"""


def to_json_string(my_obj):
    """
    transforms an object in a json representation

    Arguments:
        my_obj: a python object

    Return:
        a json representation no error checking
    """
    return json.dumps(my_obj)
