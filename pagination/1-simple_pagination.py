#!/usr/bin/env python3
"""
Pagination module: defines a Server class and a helper function
to compute pagination indices.
"""

import csv
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset loaded from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on the page number and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive int"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive int"

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end]
