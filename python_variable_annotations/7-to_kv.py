#!/usr/bin/env python3
"""
This module provides a function that
creates a key-value pair as a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the
    square of a number.

    Parameters:
    k (str): The string key.
    v (Union[int, float]): The value to square.

    Returns:
    Tuple[str, float]: A tuple where the first element is k,
    and the second is the square of v as a float.
    """
    return k, float(v ** 2)
