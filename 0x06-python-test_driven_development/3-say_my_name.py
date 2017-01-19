#!/usr/bin/python3
"""
This is the module 3-say_my_name

This module contains only on function: say_my_name.
A test suite has been built for this module, it is in /tests directory
you could call it with
python3 -m doctest -v ./tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name of a person

    Arguments:
        first_name: must be a string
        last_name: must be a string, or could not be present
                   default value = empty string

    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if last_name or last_name is None:
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
