#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate over the elements of the input list
    for item in my_list:
        # Check if the current element is equal to the search element
        if item == search:
            # If it is, append the replace element to the new list
            new_list.append(replace)
        else:
            # If it's not, append the current element as it is to the new list
            new_list.append(item)

    return new_list
