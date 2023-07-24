#!/usr/bin/python3
"""Defines a function that checks a class."""


def is_same_class(obj, a_class):
    """Checks if object is an instance of a class,
    Returns true if object is an instance of the
    class, else returns false"""
    return (type(obj) == a_class)
