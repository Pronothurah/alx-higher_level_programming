#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list.
    Args:
        my_list: A list of integers to be printed.
        idx: index to be retrieved
    Returns:
        None or element at index
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
