#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        print("0{}".format(i), end=", ")
    elif (10 < i <= 98):
        print("{}".format(i), end=", ")
    else:
        print("{}".format(i), end="")
