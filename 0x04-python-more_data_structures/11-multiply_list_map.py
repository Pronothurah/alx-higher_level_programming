#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    returns a list with all values
    multiplied by a number
    Args:
        my_list=[]: initial list
        number=0: number to multiply with
    Returns:
        Multiplied list
    """
    return list(map((lambda i: i * number), my_list))
