#!/usr/bin/python3
def uniq_add(my_list=[]):
	uni = set(my_list)
	n = 0
	for i in uni:
		n += i
	return n