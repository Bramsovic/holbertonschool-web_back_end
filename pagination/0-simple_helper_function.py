#!/usr/bin/env python3
"""
This module provides a function to compute start and end indexes
for pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start and end indexes for a given page
    and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) to slice a list.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
