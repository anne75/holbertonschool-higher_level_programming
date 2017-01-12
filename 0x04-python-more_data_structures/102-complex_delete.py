#!/usr/bin/python3


def complex_delete(my_dict, value):
    """
    delete all keys with a specific value in a dictionary

    my_dict: a dictionary
    value: value to remove

    Return: the dictionary
    """
    keys = [k for k, v in my_dict.items() if v == value]
    for k in keys:
        del my_dict[k]
    return (my_dict)
