#!/usr/bin/python3
""" is_same_class module """


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
