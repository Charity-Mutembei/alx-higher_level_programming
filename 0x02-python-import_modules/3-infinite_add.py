#!/usr/bin/python3
import sys

args = sys.argv[1:]

if __name__ == "__main__":
    
    sum_numbers = 0
    for i in args:
        sum_numbers += int(i)
    print(sum_numbers)

