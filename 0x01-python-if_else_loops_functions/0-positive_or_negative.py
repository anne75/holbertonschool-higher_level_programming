#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{:d} is ".format(number), end="")
if number > 0:
    print("positive")
elif number == 0:
    print("")
else:
    print("negative")
