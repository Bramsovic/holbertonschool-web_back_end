#!/usr/bin/env python3
"""This module provides a Redis-backed cache for storing simple values."""
import uuid
from typing import Callable, Optional, Union

import redis


DataType = Union[str, bytes, int, float]
ReturnType = Union[str, bytes, int, float]


class Cache:
    """Cache stores supported Python values in Redis under random keys."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear the active database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: DataType) -> str:
        """Store data in Redis using a random key and return that key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable[[bytes], ReturnType]] = None
            ) -> Optional[ReturnType]:
        """Retrieve Redis data by key and optionally convert the result."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve Redis data by key and decode the value as a string."""
        return self.get(key, lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve Redis data by key and convert the value to an integer."""
        return self.get(key, int)
