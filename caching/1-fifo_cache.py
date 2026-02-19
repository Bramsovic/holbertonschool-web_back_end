#!/usr/bin/env python3
"""FIFO cache module."""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Cache system with FIFO eviction policy."""

    def put(self, key, item):
        """Store an item in the cache using FIFO eviction."""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Retrieve an item by key from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key)
