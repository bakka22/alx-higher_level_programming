#!/usr/bin/python3
def number_keys(a_dictionary):
    n = 0
    ls = list(a_dictionary.keys())
    for i in ls:
        n += 1
    return n
