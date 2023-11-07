#!/usr/bin/python3
""" geometry module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """special method
        args:
            self: ...
            width: ...
            height: ...
        Returns:
            nothing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
