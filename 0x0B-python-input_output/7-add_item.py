#!/usr/bin/python3
"""Module script that adds all arguments to a Python list,
and then save them to a file:
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list(arguments, filename):
    try:
        initial_data = load_from_json_file(filename)
    except FileNotFoundError:
        initial_data = []

    initial_data.extend(arguments)
    save_to_json_file(initial_data, filename)


if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Usage: python script.py argument1 argument2 ...")
    else:
        filename = 'add_item.json'
        add_arguments_to_list(arguments, filename)
        print(f"Arguments added to {filename}: {arguments}")
