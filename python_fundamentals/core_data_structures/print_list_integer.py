#!/usr/bin/env python3
"""Print all integers in a list."""


def print_list_integer(my_list=[]):
    """Print every integer in my_list on a separate line."""
    for number in my_list:
        print("{:d}".format(number))
