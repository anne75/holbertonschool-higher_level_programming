#!/usr/bin/python3


def safe_print_integer(value):
    """
    print an integer
    throw an error if the vlue is not an int

    value: anything

    Return: True if value is an int, False otherwise
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)
    else:
        return (True)
