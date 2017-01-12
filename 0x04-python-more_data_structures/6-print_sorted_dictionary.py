#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    """
    print a dictionary with strings as keys in alphabetical order

    my_dict: a dictionary
    """
    if my_dict:
        new = ["{}: {}".format(k, my_dict[k]) for k in sorted(my_dict.keys())]
        print("\n".join(new))


# maybe would be nicer to sort case blind
# key=lambda x:(x.tolower())
