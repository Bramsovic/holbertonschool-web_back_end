#!/usr/bin/env python3
"""
Async generator that yields 10 random float values between 0 and 10.
"""
import random
import asyncio


async def async_generator():
    """
    Asynchronous generator that yields 10 random float values between
    0 and 10, with a 1-second asynchronous pause between each yield.

    This function uses asyncio to sleep asynchronously for 1 second
    in each iteration, and the random module to generate a float
    between 0 and 10 (exclusive).

    Yields:
        float: A random float between 0 and 10.
    """
    count = 0
    while count < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        count += 1
