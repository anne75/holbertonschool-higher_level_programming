#!/usr/bin/python3


def multiple_returns(sentence):
    """
    return the length and first character of a sentence
    """
    size = len(sentence)
    return (size, None if size == 0 else sentence[0])
