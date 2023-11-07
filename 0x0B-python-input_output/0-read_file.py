#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
