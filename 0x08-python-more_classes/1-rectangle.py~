#!/usr/bin/python3

""" rectangle module """


class Rectangle:
    """ this class defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        the special __init__ method

        args:
            self: refrence to instance
            width: width of the rectangle
            height: height of the rectangle
        Returns:
            nothing
        """
        err = ["space holder", "width", "height"]
        a = 0
        if not isinstance(width, int):
            a = 1
        if not isinstance(height, int):
            a = 2
        if a:
            raise TypeError(f"{err[a]} must be an intger")
        if width < 0:
            a = 1
        if height < 0:
            a = 2
        if a:
            raise ValueError(f"{err[a]} must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width setter and getter
        args:
            self: ....
            value: ....
        Returns:
            value
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height setter and getter
        args:
            self: ....
            value: ....
        Returns:
            value
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an intger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
