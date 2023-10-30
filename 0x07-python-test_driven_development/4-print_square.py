#!/usr/bin/python3
"""Module for print_square method"""


def print_square(size):
    """
    prints a square with the character #.
    Args:
        size: size of square
    Returns:
        printed square
    Raises:
        TypeError and Value Error
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + '\n') * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
