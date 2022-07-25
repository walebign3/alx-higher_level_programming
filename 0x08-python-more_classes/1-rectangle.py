#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Class Rectangle """
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)

    def set_width (self, width):
        if (type(width) != int):
            raise ValueError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        self._width = width
    def set_height (self, height):
        if (type(height) != int):
            raise ValueError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self._height = height
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height

    width = property(fget = get_width, fset = set_width)
    height = property(fget = get_height, fset = set_height)
