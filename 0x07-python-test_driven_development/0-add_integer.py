#!/usr/bin/python3
""" add_integer module """


def add_integer(a, b=98):
    """ adds two intgers
    args:
        a: first integer
        b: second integer
    raises:
        TypeError when a or b are not integers
    Returns:
        the sum of the two integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
