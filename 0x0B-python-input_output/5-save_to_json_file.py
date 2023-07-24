#!/usr/bin/python3
"""Writes a function that writes into a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
