#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                numerator = float(my_list_1[i])
                denominator = float(my_list_2[i])
                if denominator == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(numerator / denominator)
            except IndexError:
                result.append(0)
                print("out of range")
            except (ValueError, TypeError):
                result.append(0)
                print("wrong type")
    finally:
        return result
