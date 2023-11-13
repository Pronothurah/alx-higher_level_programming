#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        """width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def y(self):
        """y of rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    @property
    def x(self):
        """x of rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    def validate_integer(self, name, value, eq=True):
        """
        Method for validating all setter methods and instantiation

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Computes area of rectangle"""

        return self.__height * self.__width

    def display(self):
        """
        Display the rectangle based on width, height, x and y and character #
        """

        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        returns string info about the rectangle
        """

        return '[{}] ({}) {}/{} - {}/{}'.format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height)

    def update(self, *args, **kargs):
        """
        Update the rectangle attributes based on
        *args (non-keyword arguments) or **kwargs (keyword arguments)
        """

        if (args is not None and len(args) > 0):
            i = 0
            attributes = ["id", "width", "height", "x", "y"]
            for arg in args:
                try:
                    setattr(self, attributes[i], arg)
                    i += 1
                except IndexError:
                    pass
        else:
            for k, v in kargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Convert class to dictionnary
        """
        attributes = ["id", "width", "height", "x", "y"]
        response = {}
        for attr in attributes:
            response[attr] = getattr(self, attr)
        return response
