#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number > 0):
    last = (number % 10)
elif (number < 0):
    last = -(-number % 10)
else:
    last = 0
# implementation of the needed string
if (last > 5):
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif (last == 0):
    print(f"Last digit of {number:d} is {last:d} and is 0")
else:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
