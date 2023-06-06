#!/usr/bin/python3
"""
a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print the text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    Returns:
        None
    """
    # Check if the input is not a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces from the text
    text = text.strip()

    # Check if the text is empty
    if not text:
        return

    # Iterate over each character in the text
    for char in text:
        # Print the character
        print(char, end='')

        # Check if the character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            # Print two new lines after the character
            print("\n\n", end='')
