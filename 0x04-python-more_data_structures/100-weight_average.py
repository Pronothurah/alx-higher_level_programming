#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    return sum(a * b for a, b in my_list) / sum(b for a, b in my_list)
