#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = list(a_dictionary.keys())
    ls.sort()
    for i in ls:
        print("{}: {}".format(i, a_dictionary.get(i)))
