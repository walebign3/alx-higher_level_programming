#!/usr/bin/python3
""" Class Rectangle """


class Rectangle():
    """ Class Rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Class Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Class Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Class Rectangle """
        if (type(value) != int):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Class Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Class Rectangle """
        if (type(value) != int):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Function to print a Square with #
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = ['#' * self.__width for line in range(self.__height)]

        return '\n'.join(final)

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
