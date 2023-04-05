#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """Represent a rectangle"""
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Get the widt"""

        return self.__width
    
    @width.setter
    def width(self, value):
        """set the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """get the height"""
        
        return self.__height
    
    @height.setter
    def height(self, value):
        """set the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
