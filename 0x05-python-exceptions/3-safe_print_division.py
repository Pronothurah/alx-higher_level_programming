#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
    except Exception as e:
        result = None
        print("Inside result: {}".format(e))
    finally:
        if result is not None:
            print("Inside result: {:0.2f}".format(result))
        return result
