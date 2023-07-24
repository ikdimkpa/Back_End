#!/usr/bin/python3
"""Defines a subclass of class MyList."""


class MyList(list):
    """This class is a subclass of the list class."""

    def print_sorted(self):
        """Print a sorted list in a specific pattern."""
        print(sorted(self))
