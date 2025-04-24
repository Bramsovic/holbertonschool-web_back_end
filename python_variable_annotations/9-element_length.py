#!/usr/bin/env python3
"""
This module defines a function that returns
the length of each element in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each
    element from the input iterable and the length of that element.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequence-like elements.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    an element from the input and its length.
    """
    return [(i, len(i)) for i in lst]
