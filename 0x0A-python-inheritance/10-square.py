#!/usr/bin/python3
""" geometry module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle """

    def __init__(self, size):
        """special method
        args:
            self: ...
            size: ...
        Returns:
            nothing
        """
        Rectangle.__init__(self, size, size)
