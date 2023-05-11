#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    total = len(names)

    for i in range(total):
        if names[i][:2] != '__':
            print(names[i])
