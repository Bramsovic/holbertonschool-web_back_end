#!/usr/bin/env python3
"""
This module provides a function that returns
a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float
    by a specified multiplier.

    Parameters:
    multiplier (float): The multiplier value to use.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    the product of that float and the multiplier.
    """
    def new_function(x: float) -> float:
        return x * multiplier
    return new_function
