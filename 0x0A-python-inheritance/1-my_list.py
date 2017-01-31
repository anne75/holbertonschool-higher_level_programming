#!/usr/bin/python3
"""
This is module 1-my_list

This module contains one class
A test suite has been developed for this class in the /tests folder
run it with python3 -m doctest ./tests/1-my_list.txt
"""


class MyList(list):
    """
    Inherits from the list class

    Assumes all the elements in the list are int
    """

    def print_sorted(self):
        """print the list in sorted order"""
        print("[" + ", ".join("{:d}".format(i) for i in sorted(self)) + "]")
