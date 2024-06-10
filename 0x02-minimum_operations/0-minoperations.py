#!/usr/bin/python3
"""
Module for calculating the fewest number
of operations needed to result in n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations
    needed to result in n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
