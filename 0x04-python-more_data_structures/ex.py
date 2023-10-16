#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary)
    new = {}
    for i in key_list:
        new[i] = a_dictionary[i]
    return (new)
