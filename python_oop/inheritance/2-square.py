#!/usr/bin/env python3
"""Defines the Square class."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represents a square with a string description."""

    def __str__(self):
        """Returns a readable square description."""
        return "[Square] {0}/{0}".format(self._Square__size)
