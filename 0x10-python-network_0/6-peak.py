#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    start = 0
    stop = len(list_of_integers) - 1

    while start < stop:
        center = (start + stop) // 2

        if list_of_integers[center] < list_of_integers[center + 1]:
            start = center + 1
        else:
            stop = center

    return list_of_integers[start]
