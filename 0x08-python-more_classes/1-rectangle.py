#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Class Rectangle """
    def __init__(self, width=0, height=0):
        """ Class Rectangle """
        self._width = width
        self._height = height

    @property
    def width(self):
        """ Class Rectangle """
        return self._width

    @width.setter
    def width(self, value):
        """ Class Rectangle """
        if (type(value) != int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """ Class Rectangle """
        return self._height

    @height.setter
    def height(self, value):
        """ Class Rectangle """
        if (type(value) != int):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self._height = value

