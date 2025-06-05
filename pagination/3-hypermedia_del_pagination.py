#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any
"""
importing module csv, math and list
"""


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with hypermedia pagination information that is
        resilient to deletion in the dataset.

        Args:
            index (int): The starting index of the page (default: 0)
            page_size (int): The size of the page (default: 10)
        Returns:
            Dict: Dictionary containing pagination information
        """
        if index is None:
            index = 0

        indexed_data = self.indexed_dataset()

        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "Index is out of range"

        data = []
        next_index = index
        count = 0

        while count < page_size and next_index < len(self.dataset()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                count += 1
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
