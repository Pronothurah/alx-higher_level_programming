#!/usr/bin/python3
for character in range(ord('a'), ord('z') + 1):
    if character != ord('q') and character != ord('e'):
        print("{:c}".format(character), end="")
