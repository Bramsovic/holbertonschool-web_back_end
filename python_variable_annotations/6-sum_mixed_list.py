#!/usr/bin/env python3
"""
This module provides a function that sums a list
containing both integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all values in a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
    float: The total sum as a floating-point number.
    """
    return sum(mxd_lst)
