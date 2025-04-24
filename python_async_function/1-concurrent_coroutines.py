#!/usr/bin/env python3
"""
This module contains an async function that executes multiple coroutines
concurrently and returns the delays in ascending order.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        List[float]: List of delays, in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
