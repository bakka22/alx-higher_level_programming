#!/usr/bin/python3
""" Square module """


class Square:
    """ define a square """
    def __init__(self, sz=0):
        """ initialize class with args.

        args:
            self: the opj itself
            sz: size

        Returns:
            nothing

        """
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz

    def area(self):
        """ calculate area of the square

        args:
            self: the opject

        Returns:
            the area of the square

        """
        return self.__size ** 2

    @property
    def size(self):
        """ retrives size
        args:
            self: opject
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size
        args:
            self: object
            value: new value
        Returns:
            nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
