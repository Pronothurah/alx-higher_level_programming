#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    find multiples of 2 in a list.
    Args:
        my_list: integer list
    Returns:
        true if multiple false if otherwise
    """
    if len(my_list) < 1:
        return None
    list_copy = []
    for i in my_list:
        list_copy.append(i % 2 == 0)
    return list_copy