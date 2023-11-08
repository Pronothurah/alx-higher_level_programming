#!/usr/bin/python3
"""Module for append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after
    each line containing a specific string"""
    line_list = []

    with open(filename, 'r', encoding="utf-8") as a_file:
        for line in a_file:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'a', encoding="utf-8") as a_file:
        a_file.writelines(line_list)
