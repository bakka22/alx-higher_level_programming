#!/usr/bin/python3
""" json """


import json


def load_from_json_file(filename):
    """ return json string representaion """
    with open(filename, "w", encoding="utf-8") as w:
        json.load(w)
