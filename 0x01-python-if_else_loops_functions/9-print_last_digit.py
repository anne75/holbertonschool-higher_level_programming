#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    print("{:d}".format(n), end="")
    return (n)
