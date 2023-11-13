#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """A representation of the base class of the OOP hireachy"""

    __nb_objects = 0
    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
