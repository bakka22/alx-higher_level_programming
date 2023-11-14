#!/usr/bin/python3
""" test module for rectangle """


import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectTest(unittest.TestCase):
	""" test class for Rectangle """

	def test_inherit(self):
		""" test inherit from base """
		self.assertEqual(Rectangle.__bases__, (Base, ))

	def test_has_attr(self):
		""" test presence of attr """
		re = Rectangle(22, 5)
		self.assertTrue(hasattr(re, "width"), True)
		self.assertTrue(hasattr(re, "height"), True)
		self.assertTrue(hasattr(re, "id"), True)
		self.assertTrue(hasattr(re, "x"), True)
		self.assertTrue(hasattr(re, "y"), True)

if __name__ == "__main__":
	unittest.main()
