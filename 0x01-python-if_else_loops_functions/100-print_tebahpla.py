#!/usr/bin/python3
for i in range(90, 64, -1):
    letter = chr(i)
    if i % 2 == 0:
        letter = letter.lower()
    print("{}{}".format(letter, ""), end="")
