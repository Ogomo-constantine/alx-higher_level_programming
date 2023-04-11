#!/usr/bin/python3
"""
Module for Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special type of rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.
        """
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
