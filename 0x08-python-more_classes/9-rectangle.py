#!/usr/bin/python3

""" rectangle module """


class Rectangle:
    """ this class defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        the special __init__ method

        args:
            self: refrence to instance
            width: width of the rectangle
            height: height of the rectangle
        Returns:
            nothing
        """
        err = ["space holder", "width", "height"]
        a = 0
        if not isinstance(width, int):
            a = 1
        elif not isinstance(height, int):
            a = 2
        if a:
            raise TypeError(f"{err[a]} must be an integer")
        if width < 0:
            a = 1
        elif height < 0:
            a = 2
        if a:
            raise ValueError(f"{err[a]} must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width setter and getter
        args:
            self: ....
            value: ....
        Returns:
            value
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height setter and getter
        args:
            self: ....
            value: ....
        Returns:
            value
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of a rectangle
        args:
            self: ...
        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of the rectangle
        args:
            self: ....
        Returns:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ special str method
        args:
            self
        Returns:
            string representation of an object
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        tmp = ""
        for i in range(self.__height):
            for j in range(self.__width):
                tmp += "#"
            if i != self.__height - 1:
                tmp += "\n"
        return tmp

    def __repr__(self):
        """ special repe method
        args:
            self: ....
        Returns:
            str representation of object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare 2 rectangles
        args:
            rect_1: ....
            rect_2: ....
        Returns:
            the biggest rect
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ square method
        args:
            cls: the rectangle class
            size: size of the square
        Returns:
            new instance of a Rectangle
        """
        return cls(size, size)

    def __del__(self):
        """ special __del__ destructor
        args:
            self: ....
        Returns:
            a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
