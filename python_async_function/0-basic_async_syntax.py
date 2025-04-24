#!/usr/bin/env python3
"""
Async coroutine that waits a random delay and returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay (inclusive) seconds
    and returns the delay.

    Args:
        max_delay (int): The maximum number of
        seconds to wait. Defaults to 10.

    Returns:
        float: The random delay that was waited,
        as a float number of seconds.
    """
    time = random.uniform(0.1, max_delay)
    await asyncio.sleep(time)
    return time
