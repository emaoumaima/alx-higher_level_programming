#!/usr/bin/python3
"""
This module contains the function add_integer.
"""


def add_integer(a, b=98):
    """
    Add two integers together.

    Parameters:
    a (int or float): The first number. Must be an integer or float.
    b (int or float): The second number. Must be an integer or float.

    Returns:
    int: The sum of a and b, as an int.
    """
    if isinstance(a, (int, float)):
        if a != a or abs(a) == float('inf'):
            raise TypeError("a must be an integer")
        else:
            a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        if b != b or abs(b) == float('inf'):
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
