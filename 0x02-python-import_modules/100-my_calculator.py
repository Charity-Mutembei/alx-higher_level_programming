#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    def print_usage():
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    def perform_operation(a, operator, b):

        if operator == '+':
            result = add(a, b)
        if operator == '-':
            result = sub(a, b)
        if operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)
        else:
            print("Unknown Operator")
        
        print(f"{a} {operator} {b} = {result}")

    if len(sys.argv) != 4:
        print_usage()

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    perform_operation(a, operator, b)
