#!/usr/bin/python3
"""Writes a function that appends text to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
