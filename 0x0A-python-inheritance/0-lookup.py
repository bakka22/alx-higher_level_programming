""" look up module """


def lookup(obj):
    """ lookup function
    args:
        obj: object to look at
    Returns:
        list of available attributes and methods of an object
    """
    return dir(obj)
