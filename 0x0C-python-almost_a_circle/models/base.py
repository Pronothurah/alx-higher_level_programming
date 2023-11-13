#!/usr/bin/python3
"""Module for Base class"""
from json import dumps, loads
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a list of dictionaries"""

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON representation to JSON object
        """

        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves jsonified object to file
        """

        name = "{}.json".format(cls.__name__)
        if list_objs is not None:
            list_objs = [obj_item.to_dictionary() for obj_item in list_objs]
        with open(file=name, mode='w', encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(list_objs))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a file as csv representation
        """
        items = []
        name = "{}.csv".format(cls.__name__)
        if (list_objs is not None):
            for item in list_objs:
                temp = []
                for _, j in item.to_dictionary().items():
                    temp.append(str(j))
                items.append(",".join(temp))

        with open(file=name, mode="w", encoding="utf-8") as file:
            if (len(items) == 0):
                file.write("[]")
            else:
                for item in items:
                    print(item, file=file)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance from a dictionary

        Returns:
            newly created instance of class
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from file; unjsonfies"""
        from os import path

        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, 'r', encoding='utf-8') as a_file:
            return [cls.create(**d) for d
                    in cls.from_json_string(a_file.read())]

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square

        result = []
        file = "{}.csv".format(cls.__name__)

        with open(file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {'id': row[0], 'width': row[1], 'height': row[2],
                         'x': row[3], 'y': row[4]}
                else:
                    d = {'id': row[0], 'size': row[1],
                         'x': row[2], 'y': row[3]}
                result.append(cls.create(**d))

        return result
