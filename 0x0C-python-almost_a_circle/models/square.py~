#!/usr/bin/python3
""" square module """

from rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ special __init__ method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ special __str__ method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ size setter and getter """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update attributes """
        if args is None or args == ():
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "size":
                    self.size = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """ return dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y}
