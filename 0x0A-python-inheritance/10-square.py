#!/usr/bin/python3
"""Defines a subclass/child Square of class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initializes a new square.
        Args:
            size (int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
