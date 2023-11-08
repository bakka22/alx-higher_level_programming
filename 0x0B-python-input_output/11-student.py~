#!/usr/bin/python3
""" student class """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ initialize the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ json reprisentation """
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic
