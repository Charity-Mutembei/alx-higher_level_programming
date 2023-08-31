#!/usr/bin/python3
"""
function that finds the peak number in a list
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.
    """

    def binary_search_peak(arr, low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        if arr[mid] >= arr[mid + 1]:
            return binary_search_peak(arr, low, mid)
        else:
            return binary_search_peak(arr, mid + 1, high)

    if not list_of_integers:
        return None

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
