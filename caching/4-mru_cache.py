#!/usr/bin/env python3
"""MRU cache module."""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Cache system with MRU eviction policy."""

    def __init__(self):
        """Initialize MRU cache."""
        super().__init__()
        self._usage_order = []

    def put(self, key, item):
        """Store an item in the cache using MRU eviction."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._usage_order.remove(key)
            self._usage_order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self._usage_order.pop()
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self._usage_order.append(key)

    def get(self, key):
        """Retrieve an item by key from the cache."""
        if key is None or key not in self.cache_data:
            return None

        self._usage_order.remove(key)
        self._usage_order.append(key)
        return self.cache_data[key]
