#!/usr/bin/env python3
"""Demonstrates inheritance and polymorphism."""


class Animal:
    """Represents an animal."""

    def speak(self):
        """Returns a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog."""

    def speak(self):
        """Returns the dog sound."""
        return "Woof"


class Cat(Animal):
    """Represents a cat."""

    def speak(self):
        """Returns the cat sound."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())
