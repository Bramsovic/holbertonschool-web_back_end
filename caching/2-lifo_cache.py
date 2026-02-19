#!/usr/bin/env python3
"""LIFO cache module."""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Cache system with LIFO eviction policy."""

    def __init__(self):
        """Initialize LIFO cache."""
        super().__init__()
        self._put_order = []

    def put(self, key, item):
        """Store an item in the cache using LIFO eviction."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._put_order.remove(key)
            self._put_order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self._put_order.pop()
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self._put_order.append(key)

    def get(self, key):
        """Retrieve an item by key from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key)
