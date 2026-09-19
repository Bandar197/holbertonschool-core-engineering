#!/usr/bin/env python3
"""Calculate powers without using the exponent operator."""


def pow(a, b):
    """Return a raised to the power b."""
    result = 1
    exponent = b

    if exponent < 0:
        exponent = -exponent

    for _ in range(exponent):
        result *= a

    if b < 0:
        return 1 / result

    return result
