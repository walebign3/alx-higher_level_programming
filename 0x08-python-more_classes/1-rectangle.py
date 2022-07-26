#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Class Rectangle """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Class Rectangle """
        return self._width

    @property
    def height(self):
        """ Class Rectangle """
        return self._height

    @width.setter
    def width(self, width):
        """ Class Rectangle """
        if (type(width) != int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        self._width = width

    @height.setter
    def height(self, height):
        """ Class Rectangle """
        if (type(height) != int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self._height = height

"""    width = property(fget = get_width, fset = set_width)
    height = property(fget = get_height, fset = set_height)
"""
