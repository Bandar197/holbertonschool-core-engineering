#!/usr/bin/env python3
"""Defines an abstract Animal class and concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represents an abstract animal."""

    @abstractmethod
    def sound(self):
        """Returns the sound produced by the animal."""
        pass


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
