#!/usr/bin/python3


def no_c(mystr):
    """
    removes all letter c from a string
    DO NOT use s t r . r e p l a c e

    """
    my_list = [letter for letter in mystr if (letter.lower() != "c")]
    return ("".join(my_list))


# better solution, Philip's, list.translate
