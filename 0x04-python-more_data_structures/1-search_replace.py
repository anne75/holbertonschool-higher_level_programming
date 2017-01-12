#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    replace some values in a list by another one

    my_list: a list
    search: element to look for
    replace: value to replace search with

    Return: new corrected list
    """
    return ([x if x != search else replace for x in my_list])
