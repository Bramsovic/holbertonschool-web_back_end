#!/usr/bin/env python3
"""This module provides a Redis-backed cache for storing simple values."""
import uuid
from typing import Union

import redis


DataType = Union[str, bytes, int, float]


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
