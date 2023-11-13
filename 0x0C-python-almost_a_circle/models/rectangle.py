#!/usr/bin/python3
""" Rectangle module """


import Base


base = Base


def ty_err(name):
    """ raises an error """
    raise TypeError("{} must be an integer".format(name))


def va_err(name, idx):
    """ raises an error """
    if idx <= 1:
        raise ValueError("{} must be > 0".format(name))
    raise ValueError("{} must be >= 0".format(name))


class Rectangle(base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ special init method """
        ar = [width, height, x, y]
        cou = ["width", "height", "x", "y"]
        for i, val in enumerate(ar):
            if not isinstance(val, int):
                ty_err(cou[i])
            if i <= 1 and val <= 0:
                va_err(cou[i], i)
            if i > 1 and val < 0:
                va_err(cou[i], i)

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def update(self, *args, **kwargs):
        """ update attributes """
        cou = ["spho", "width", "height", "x", "y"]
        if args is None or args == ():
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "width":
                    self.width = val
                if key == "height":
                    self.height = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val

        for i, arg in enumerate(args):
            if i > 0 and not isinstance(arg, int):
                ty_err(cou[i])
            if i > 0 and i < 3 and arg <= 0:
                va_err(cou[i], i - 1)
            if i > 2 and arg < 0:
                va_err(cou[i], i - 1)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ print rectangle using '#' character """
        for w in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def to_dictionary(self):
        """ return the dictionary rep of the rect """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """ width setter and getter """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            ty_err("width")
        if value <= 0:
            va_err("width", 0)
        self.__width = value

    @property
    def height(self):
        """ height getter and setter """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            ty_err("height")
        if value <= 0:
            va_err("height", 1)
        self.__height = value

    @property
    def x(self):
        """ x getter and setter """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            ty_err("x")
        if value < 0:
            va_err("x", 2)
        self.__x = value

    @property
    def y(self):
        """ y getter and setter """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            ty_err("y")
        if value < 0:
            va_err("y", 3)
        self.__y = value

    def __str__(self):
        """ special __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
