#!/usr/bin/python3
import sys
args = sys.argv[1:]
num_args = len(args)
if __name__ == "__main__":

    if num_args == 0:
        print(num_args, "arguments.")
    elif num_args == 1:
        print(num_args, "argument:")
        for i, arg in enumerate(args, start=1):
            print(i, ":", arg)
    else:
        print(num_args, "arguments:")
        for i, arg in enumerate(args, start=1):
            print(i, ":", arg)
