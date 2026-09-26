#!/usr/bin/env python3
"""Demonstrates multiple inheritance with a flying fish."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Prints the swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Prints the flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a fish that can also fly."""

    def fly(self):
        """Prints the flying fish flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints the flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
