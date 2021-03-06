#!/usr/bin/python3
"""Magic module"""
import math


class MagicClass:
    """
    This is a class of MagicClass
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ function area """
    def area(self):
        return (self.__radius ** 2) * math.pi

    """ function circumference"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
