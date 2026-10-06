#!/usr/bin/env python3
"""Write text to a file"""


def write_file(filename="", text=""):
    """Write text and return nb of char written"""
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)

    return count
