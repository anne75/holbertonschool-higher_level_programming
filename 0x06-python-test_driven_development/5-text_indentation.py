#!/usr/bin/python3
"""
This is the module 5-text_indentation

This module contains only one function text_indentation
This module has a test suite in the directory ./tests
You can run it with  python3 -m doctest ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Replaces a space after ., ? and : with 2 newlines in a string, prints the result

    Argument:
       text: a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = []
    flag = False
    for i, letter in enumerate(text):
        if letter in ".?:":
            new.append("{}\n\n".format(letter))
            flag = True
        else:
            if not flag:
                new.append(letter)
            else:
                flag = False
                if not letter == " ":
                    new.append(letter)

    print("".join(new), end="")
