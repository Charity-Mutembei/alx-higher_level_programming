#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of the given number and returns it.
    """
    # get the absolute value of the number to handle negative inputs
    abs_number = abs(number)

    # get the last digit of the absolute number using the modulo operator
    last_digit = abs_number % 10

    # print the last digit using a print statement
    print(last_digit, end="") 
    # return the last digit
    return last_digit

