#!/usr/bin/python3
""" Square module """


class Square:
    """ define a square """
    def __init__(self, sz=0, position=(0, 0)):
        """ initialize class with args.

        args:
            self: the opj itself
            sz: size

        Returns:
            nothing

        """
        if (not isinstance(position, tuple)) or
        not (position[0] < 0 and position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(sz, int):
            raise TypeError("size must be an integer")
        if sz < 0:
            raise ValueError("size must be >= 0")
        self.__size = sz
        self.__position = position

    def area(self):
        """ calculate area of the square

        args:
            self: the opject

        Returns:
            the area of the square

        """
        return self.__size ** 2

    @property
	def position(self):
		""" retrives position
		args:
			slef: object
		Returns:
			position
		"""
		return self.__position

	@position.setter
	def position(self, value):
		if (not isinstance(value, tuple)) or
		not (value[0] < 0 and value[1] < 0):
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

    @property
    def size(self):
        """ retrives size
        args:
            self: opject
        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size
        args:
            self: object
            value: new value
        Returns:
            nothing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ print square
        args:
            self: opject
        Returns:
            nothing
        """
        x = self.__size
        for i in range(x):
            for y in range(self.__position[0]):
		print(end=" ")
            for j in range(x):
                print("#", end="")
            print()
        if x == 0:
            print()
