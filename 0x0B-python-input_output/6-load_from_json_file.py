#!/usr/bin/python3
""" json """


import json


def load_from_json_file(filename):
    """ return json string representaion """
    with open(filename, "r", encoding="utf-8") as w:
        return json.load(w)
