#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    print the first x elements of a list only if they are ints

    my_list: a list
    x: number of elements to print

    Return: the number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (count)
