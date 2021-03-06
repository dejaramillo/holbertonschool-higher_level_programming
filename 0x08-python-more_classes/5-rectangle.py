#!/usr/bin/python3
"""
This module provides a Rectange class
"""


class Rectangle:
    """
    Class of Rectangle

    Attributes:
        attr1 (width): width of the rectangle
        attr2 (height): height of the rectangle
        attr3 (area): method that returns the area of the rectangle
        attr4 (perimeter): method that returns the perimeter of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructor of the class

        Args:
            param1 (width): width of the rectangle
            param2 (height): height of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This is a getter of the class
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This is a getter of the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        Function that calculates the area of the rectangle

        Returns:
           Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Function that calculates the perimeter of the rectangle

        Returns:
           Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        str1 = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str1 += "#"
            str1 += "\n"

        return str1[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
