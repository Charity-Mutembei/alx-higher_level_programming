#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if a_dictionary is None
    if a_dictionary is None:
        return None

    # Initialize variables to store the best key and value
    best_key = None
    best_value = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is the best so far
        if best_value is None or value > best_value:
            # Update the best key and value
            best_key = key
            best_value = value

    return best_key
