#!/usr/bin/env python3
"""this file use append"""


def append_write(filename="", text=""):
    """this function use a to add contant without  old contant"""
    with open(filename, "a", encoding="utf-8") as f:
        append = f.write(text)

    return append
