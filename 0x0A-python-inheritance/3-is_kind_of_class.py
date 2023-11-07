#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ chek if object is instance of a class
    args:
        obj: object
        a_class: class
    Returns:
        True or False
    """
    return isinstance(obj, a_class)
