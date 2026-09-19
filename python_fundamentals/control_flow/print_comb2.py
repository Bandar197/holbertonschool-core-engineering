#!/usr/bin/env python3
"""Print numbers from 00 to 99."""

for number in range(100):
    if number == 99:
        print("{:02d}".format(number))
    else:
        print("{:02d}, ".format(number), end="")
