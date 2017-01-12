#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    returns the moyenne ponderee of all integer tuples

    list of (number, coefficient) tuples

    Return: average or 0 if list is empty
    """
    average = 0
    if my_list:
        average = sum(x[0] * x[1] for x in my_list)/sum(x[1] for x in my_list)
    return (average)
