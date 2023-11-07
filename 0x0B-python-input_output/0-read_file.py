#!/usr/bin/python3
""" read_file function """

def read_file(filename=""):
	""" read_file
	args:
		filename: name of the file
	Returns:
		nothing
	"""
	with open(filename, encoding='utf-8') as w:
		print(w.read(), end="")
