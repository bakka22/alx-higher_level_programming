#!/usr/bin/python3
""" base module """


import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ special init method """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json string to file """
        x = []
        for i in list_objs:
            x.append(i.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        """ return a list from json string """
        if json_string is None:
            return []
        x = json.loads(json_string)
        if not isinstance(x, list):
            return []
        return x

    @classmethod
    def create(cls, **dictionary):
        """ create a new instance """
        x = 0
        if cls.__name__ == "Rectangle":
            x = cls(1, 1)
        elif cls.__name__ == "Square":
            x = cls(1)
        else:
            x = cls()
        if "update" in dir(cls):
            x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """ return a alist of instances """
        y = []
        try:
            with open(f"{cls.__name__}.json") as f:
                x = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        for i in x:
            y.append(cls.create(**i))
        return y

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw rectangles and squares """
        turtle.bgcolor("black")
        t = turtle.Turtle()
        t.ht()
        color = ['red', 'yellow', 'blue', 'green']
        for item in list_rectangles + list_squares:
            turtle.bgcolor("black")
            x = 0
            t.pencolor(color[x])
            t.forward(item.width)
            t.right(90)
            x += 1
            t.pencolor(color[x])
            t.fd(item.height)
            t.right(90)
            x += 1
            t.pencolor(color[x])
            t.forward(item.width)
            t.right(90)
            x += 1
            t.pencolor(color[x])
            t.fd(item.height)
            time.sleep(5)
            turtle.clearscreen()
        turtle.bgcolor("black")
        turtle.done()
