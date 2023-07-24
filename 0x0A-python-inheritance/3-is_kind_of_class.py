#!/usr/bin/python3
"""Defines a class a function that checks for inherit class."""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a_class
    or a class that a_class inherits from"""
    if isinstance(obj, a_class):
        return True
    return False
