#!/usr/bin/python3
"""Module defines a class named Student"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets adictionary representation of Student"""
        return self.__dict__
