#!/usr/bin/python3


def no_c(mystr):
    """
    removes all letter c from a string
    DO NOT use str.replace()

    """
    my_list = [letter for letter in mystr if (letter.lower() != "c")]
    return ("".join(my_list))
