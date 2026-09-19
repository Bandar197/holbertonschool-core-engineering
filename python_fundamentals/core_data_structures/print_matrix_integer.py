#!/usr/bin/env python3
"""Print a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix with one row per line."""
    for row in matrix:
        for index, number in enumerate(row):
            if index == len(row) - 1:
                print("{:d}".format(number), end="")
            else:
                print("{:d} ".format(number), end="")
        print()
