#!/usr/bin/python3
# 6-from_json_string.py
"""Writes a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of JSON string."""
    return json.loads(my_str)
