#!/usr/bin/env python3
"""Module that defines an asynchronous generator yielding random float values."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random float values between
    0 and 10, with a 1-second asynchronous pause between each yield.

    Yields:
        float: A random float between 0 and 10.
    """
    count = 0
    while count < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        count += 1
