#!/usr/bin/python3
"""Function that reads a UTF-8 text file and prints it to stdout."""


def read_file(filename=""):
    """Prints the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
