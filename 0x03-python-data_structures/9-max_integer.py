#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    finds the biggest integer of a list.
    Args:
        my_list: integer list
    Returns:
        biggest integer
    """
    return max(my_list) if len(my_list) > 0 else None
