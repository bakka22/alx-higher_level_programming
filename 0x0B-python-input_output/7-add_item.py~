#!/usr/bin/python3
""" add and load from json """


import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arls = list(sys.argv[1:])

try:
    loaded_data = load_from_json_file('add_item.json')
except Exception:
    loaded_data = []

loaded_data.extend(arls)
save_to_json_file(loaded_data, 'add_item.json')
