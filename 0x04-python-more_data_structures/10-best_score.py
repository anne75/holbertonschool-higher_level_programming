#!/usr/bin/python3


def best_score(my_dict):
    """
    given a dictionary of int values return the key with the biggest value

    my_dict: a dictionary

    return: a key
    """
    if not my_dict:
        return (None)

    sorted_keys = sorted(my_dict.keys(), key=lambda x: my_dict[x],
                         reverse=True)
    return (sorted_keys[0])

# I sort the keys in the dictionary by their value
# return the first element
# or loop through dictionary...
