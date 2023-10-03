#!/usr/bin/python3
for character in range(0, 100):
    if character < 99:
        print("{:02d}".format(character), end=", ")
    else:
        print("{:d}".format(character))
