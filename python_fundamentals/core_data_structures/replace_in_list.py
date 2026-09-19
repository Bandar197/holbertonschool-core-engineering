#!/usr/bin/env python3
"""Replace an element in a list."""


def replace_in_list(my_list, idx, element):
    """Replace the element at idx and return the list."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
