#!/usr/bin/python3
""" geometry module """


class BaseGeometry:
    """ base_geometry """
    def area(self):
        """ area
        args:
            self: instnace
        Returns:
            nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator
        args:
            self: object it self
            name: key for value
            value: value of key
        Returns:
            nothing
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
