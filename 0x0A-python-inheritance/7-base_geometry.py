#!/usr/bin/python3
""" geometry module """

def is_same_class(obj, a_class):
    """ is_same_class check if object is instance of a class
    args:
        obj: the object
        a_class: the class
    Returns:
        True if the obj is instance False otherwize
    """

    x = type(obj)
    x = str(x)
    x = x[8:-2]
    if x == a_class.__name__:
        return True
    return False

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
        if not is_same_class(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
