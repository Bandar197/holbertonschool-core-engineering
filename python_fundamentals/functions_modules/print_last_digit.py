#!/usr/bin/env python3
"""Print and return the last digit of a number."""


def print_last_digit(number):
    """Print and return the positive last digit."""
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
