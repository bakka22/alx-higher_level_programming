#!/usr/bin/python3
""" inherits from module """


def inherits_from(obj, a_class):
    """ check if the object is iherent from class
    args:
        obj: object
        a_class: class
    Returns:
        True or False
    """
    list = ()
    list += type(obj).__bases__
    for j in list:
        list += j.__bases__
    for i in list:
        if i.__name__ == a_class.__name__:
            return True

    return False
