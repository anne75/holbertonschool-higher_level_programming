#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    assume the 2 tuples contain only int
    return a tuple of length 2 containing the sum
    pre element
    """
    if not tuple_a:
        return add_tuple(tuple_b, (0, 0))
    if not tuple_b:
        return add_tuple((tuple_a), (0, 0))

    x = tuple_a[0] + tuple_b[0]
    y = 0 if len(tuple_a) == 1 else tuple_a[1]
    y += 0 if len(tuple_b) == 1 else tuple_b[1]
    return (x, y)

# tuple((x + y for x, y in zip(tuple_a, tuple_b)))
# does not work, stop iterating
# David's solution better, use max(2, len)
# Best solution, Richard's a = a + (0, 0)
