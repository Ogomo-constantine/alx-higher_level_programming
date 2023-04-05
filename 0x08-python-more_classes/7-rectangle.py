#!/usr/bin/python3
"""
This module contains a Rectangle class
"""

class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with
        Args:
            - width: integer width
            - height: integer height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        returns the rectangle with "#" characters
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """
        returns a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        prints a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        getter function for private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function for private attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter function for private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for private attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
