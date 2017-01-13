#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    prints x elements of a list, or less if the list is too short

    my_list: a list, default to []
    x: number of elements to print, default to 0

    catch errors
    """
    count = 0
    while count < x:
        try:
            print("{}".format(my_list[count]), end="")
        except (IndexError, TypeError):
            break
        count += 1
    print("")
    return (count)
