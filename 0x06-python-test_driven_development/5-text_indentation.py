#!/usr/bin/python3
"""
This is the module 5-text_indentation

This module contains only one function text_indentation
This module has a test suite in the directory ./tests
You can run it with  python3 -m doctest ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Replaces a space after ., ? and : with 2 newlines in a string, prints the
    result

    Argument:
       text: a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = []
    text = text.strip()
    flag = True
    for letter in text:
        if letter in ".?:\n":
            flag = True
            if letter == "\n":
                new.append("\n")
            else:
                new.append("{}\n\n".format(letter))
        else:
            if not flag:
                new.append(letter)
            else:
                if not letter == " ":
                    new.append(letter)
                    flag = False

    print("".join(new), end="")
