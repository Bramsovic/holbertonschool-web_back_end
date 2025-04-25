#!/usr/bin/env python3
"""
This module contains a function that creates and returns an asyncio Task
to execute wait_random with a specified maximum delay.
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay time for wait_random.

    Returns:
        asyncio.Task: A Task object representing the coroutine execution.
    """
    result = asyncio.create_task(wait_random(max_delay))
    return result
