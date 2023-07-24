#!/usr/bin/python3
"""Defines a function that writes into a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write into the file.
    Returns:
        The total number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
