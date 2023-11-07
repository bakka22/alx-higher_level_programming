#!/usr/bin/python3
""" write_file function """


def append_write(filename="", text=""):
    """ read_file
    args:
        filename: name of the file
        text: ...
    Returns:
        nothing
    """
    with open(filename, "a", encoding='utf-8') as w:
        return w.write(text)
