#!/usr/bin/python3
import sys

args = sys.argv[1:]
number_args = len(args)

if __name__ == "__main__":
    
    if number_args == 0 or number_args == 1:
        print(f"{number_args}")
    else:
        sum_numbers = 0
        for i in args:
            sum_numbers += int(i)
        print(sum_numbers)

