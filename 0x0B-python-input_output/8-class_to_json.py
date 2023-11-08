#!/usr/bin/python3
""" class to json function """


def class_to_json(obj):
    """ return dictionary description """
    return obj.__dict__
