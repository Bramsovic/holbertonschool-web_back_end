#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of executing
multiple coroutines concurrently and returns the average time per coroutine.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n and return the average time.

    Args:
        n (int): Number of times to spawn wait_random via wait_n.
        max_delay (int): Maximum delay to pass to each wait_random call.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    resultat = asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time
