#!/usr/bin/python3
"""Defines an object attribute and methods using lookup function."""


def lookup(obj):
    """Returns list of an object's available attributes and methods."""
    return (dir(obj))
