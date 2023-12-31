#!/usr/bin/python3
""" test module for rectangle """


import unittest
from models.base import Base


class Base_Test(unittest.TestCase):
	""" test class for Rectangle """

	def test_inherit(self):
		""" test inherit from base """
		self.assertEqual(Base.__bases__, (object, ))

	def test_has_attr(self):
		""" test presence of attr """
		re = Base()
		self.assertTrue(hasattr(re, "id"), True)

if __name__ == "__main__":
	unittest.main()
