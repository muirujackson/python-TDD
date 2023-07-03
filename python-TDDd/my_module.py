#!/usr/bin/python3

"""
This module contains the add function only

"""

def add(a, b):

    """
    This function adds two numbers integer/float

    Args:
        a (int/float): The first number
        b (int/float): The second number

    Returns:
        int: The sum of the a and b

    Example:
        >>> add(3, 3)
        6

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an interger/float")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer/float")

    a = int(a)
    b = int(b)

    return (a + b)
