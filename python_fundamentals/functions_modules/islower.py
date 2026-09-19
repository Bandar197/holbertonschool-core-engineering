#!/usr/bin/env python3
"""Check for lowercase characters."""


def islower(c):
    """Return True if c is a lowercase ASCII letter."""
    return ord('a') <= ord(c) <= ord('z')
