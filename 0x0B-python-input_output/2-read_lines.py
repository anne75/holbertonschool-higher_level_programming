#!/usr/bin/python3
"""
This is module 2-read_lines
This module contains one function
"""


def read_lines(filename="", nb_lines=0):
    """
    reads at most a given number of lines in a file

    Arguments:
        filename: path to file
        nb_lines: number of lines to read, if negative or null, reads the whole
        file
    """
    if type(nb_lines) is not int:
        raise TypeError("nb_lines must be an int")

    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                if nb_lines > 0:
                    print(line[:-1])
                    nb_lines -= 1
                else:
                    break
