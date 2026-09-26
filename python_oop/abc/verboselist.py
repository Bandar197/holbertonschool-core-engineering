#!/usr/bin/env python3
"""Defines a verbose extension of the built-in list class."""


class VerboseList(list):
    """Represents a list that reports modification operations."""

    def append(self, item):
        """Appends an item and reports the operation."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list and reports how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Reports and removes an item from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Reports and removes an item at the given index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
