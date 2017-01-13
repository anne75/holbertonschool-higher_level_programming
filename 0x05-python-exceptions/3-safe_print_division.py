#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides 2 integers
    exercise in exception handling

    a: an int
    b: an int

    Return: the result of the division or None
    """
    try:
        c = a / b
    except (ZeroDivisionError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return (c)
