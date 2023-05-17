#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over the elements of the input list
    for num in my_list:
        # Add the current element to the set
        unique_integers.add(num)

    # Calculate the sum of the unique integers
    total_sum = sum(unique_integers)

    return total_sum
