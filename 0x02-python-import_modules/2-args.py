#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print(num_args, "arguments.")
    elif num_args == 1:
        print(num_args, "argument:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
    else:
        print(num_args, "arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")

# In this program, we import the sys module to access 
# the command-line arguments passed to the script. 
# We slice sys.argv to exclude the script name itself and 
# store the remaining arguments in the args list.

# We determine the number of arguments using len(args) and 
# store it in the num_args variable.

# Next, we check if num_args is zero. If it is, we print a single 
# dot "." to indicate no arguments were passed. Otherwise, we iterate 
# over the args list using enumerate to get both the index i and the 
# argument value arg. We start the index at 1 using the start=1 parameter
