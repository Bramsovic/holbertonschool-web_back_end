#!/usr/bin/env python3
"""This module provides a Redis-backed cache for storing simple values."""
from functools import wraps
import uuid
from typing import Any, Callable, Optional, Union

import redis


DataType = Union[str, bytes, int, float]
ReturnType = Union[str, bytes, int, float]


def count_calls(method: Callable[..., Any]) -> Callable[..., Any]:
    """Decorate a Cache method to count how many times it is called."""
    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Increment the method call count and return the method result."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable[..., Any]) -> Callable[..., Any]:
    """Decorate a Cache method to save its input and output history."""
    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        """Store the method call arguments and return value in Redis lists."""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable[..., Any]) -> None:
    """Display the call history for a decorated Cache method."""
    redis_client = method.__self__._redis
    name = method.__qualname__
    input_key = "{}:inputs".format(name)
    output_key = "{}:outputs".format(name)

    count = redis_client.get(name)
    count = int(count) if count is not None else 0
    print("{} was called {} times:".format(name, count))

    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)

    for args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            name,
            args.decode("utf-8"),
            output.decode("utf-8")
        ))


class Cache:
    """Cache stores supported Python values in Redis under random keys."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear the active database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
