#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    """
    delete an element in a dictionary using strings as keys

    my_dict: a dictionary
    key: a key

    Return: the dictionary
    """
    if key in my_dict:
        del my_dict[key]

    return (my_dict)
