#!/usr/bin/python3
""" test module for rectangle """


import unittest
from models.square import Square
from models.rectangle import Rectangle


class Square_Test(unittest.TestCase):
	""" test class for Rectangle """

	def test_inherit(self):
		""" test inherit from base """
		self.assertEqual(Square.__bases__, (Rectangle, ))

	def test_has_attr(self):
		""" test presence of attr """
		re = Square(44)
		self.assertTrue(hasattr(re, "size"), True)
		self.assertTrue(hasattr(re, "id"), True)
		self.assertTrue(hasattr(re, "x"), True)
		self.assertTrue(hasattr(re, "y"), True)

if __name__ == "__main__":
	unittest.main()
