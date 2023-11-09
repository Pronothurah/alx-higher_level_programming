#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle in class"""
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
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def y(self):
        """y of rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
    
    @property
    def x(self):
        """x of rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value