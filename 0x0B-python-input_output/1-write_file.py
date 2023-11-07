#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """ read_file
    args:
        filename: name of the file
        text: ...
    Returns:
        nothing
    """
    with open(filename, "w", encoding='utf-8') as w:
        return w.write(text)
