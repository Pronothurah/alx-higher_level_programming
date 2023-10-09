#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print all integers in a list, one integer per line.
    
    Args:
        my_list (List[int]): A list of integers to be printed.
        
    Returns:
        None
    """
    for item in my_list:
        print("{:d}".format(item))
