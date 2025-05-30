#!/usr/bin/env python3
"""
This module provides a function to sum a
list of floating-point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all the float values in the input list.
    Parameters:
    input_list (List[float]): A list of floating-point numbers.
    Returns:
    float: The total sum of the numbers in the list.
    """
    return sum(input_list)
