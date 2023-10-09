#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints a list of ints in reverse.
    Args:
        my_list[]: A list ints.
    Returns:
        Reversed list
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
