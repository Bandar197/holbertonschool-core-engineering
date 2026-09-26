#!/usr/bin/env python3
"""Demonstrates reusable behavior using mixins."""


class SwimMixin:
    """Provides swimming behavior."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon with swimming and flying behavior."""

    def roar(self):
        """Prints the dragon roaring."""
        print("The dragon roars!")
