#!/usr/bin/python3
# def fizzbuzz():
#     for n in range(1, 101):
#         if (n % 3 == 0):
#             print("Fizz", end="")
#         if (n % 5 == 0):
#             print("Buzz", end="")
#         elif (n % 3 != 0):
#             print("{:d}".format(n), end="")
#         print(" ", end="")


def helper(n):
    s = ""
    if (n % 3 == 0):
        s += "Fizz"
    if (n % 5 == 0):
        s += "Buzz"
    elif (n % 3 != 0):
        s += str(n)
    return (s)


def fizzbuzz():
    print(" ".join([helper(n) for n in range(1, 101)]), end="")
    print("{} ".format(""), end="")
