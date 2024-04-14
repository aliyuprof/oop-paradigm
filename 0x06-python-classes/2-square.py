#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """This creates an instance of a class Square.

        Args:
            size: size of the square

        Raises:
            TypeError: Size Must be an integer
            ValueError: size must be >= 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
