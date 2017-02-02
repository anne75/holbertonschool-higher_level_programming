#!/usr/bin/python3
import json
"""
This is module 7-save_to_json_file
This module contains ine function
"""


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its json representation

    Arguments:
       my_obj: a python object
       filename: path to file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
