#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list
    Args:
        my_list=[]: integer list
        idx: index to be deleted
    Returns:
        new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
