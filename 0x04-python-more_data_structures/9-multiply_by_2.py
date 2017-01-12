#!/usr/bin/python3


def multiply_by_2(my_dict):
    """
    return a new dictionary where all values are multiplied by 2
    all values are ints

    my_dict: a dictionary

    Return: a dictionary
    """
    return ({k: my_dict[k] * 2 for k in my_dict})
