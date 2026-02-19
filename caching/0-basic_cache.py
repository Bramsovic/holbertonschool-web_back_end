#!/usr/bin/env python3
"""Basic cache module."""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Cache system without eviction policy."""

    def put(self, key, item):
        """Store an item in the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key)
