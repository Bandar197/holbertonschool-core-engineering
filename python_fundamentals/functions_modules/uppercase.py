#!/usr/bin/env python3
"""Print a string in uppercase."""


def uppercase(str):
    """Print str in uppercase using ASCII conversion."""
    result = ""

    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char

    print(result)
