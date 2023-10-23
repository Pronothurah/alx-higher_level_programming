#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not message:
        message = "A custom exception with a message."
    raise NameError(message)
