#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    execute a function safely

    fct: pointer to a functiom
    args: list of arguments

    Return: result of the function or None if error occurs
    """
    result = None
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return (result)
