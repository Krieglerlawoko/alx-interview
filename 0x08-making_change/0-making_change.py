#!/usr/bin/python3
"""
Making Change Module
This module contains a function to determine the minimum number of coins
required to make a given total amount from a list of coin denominations.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): List of coin denominations.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The minimum number of coins needed to make the total amount.
             Returns 0 if total is 0 or less. Returns -1 if the total cannot
             be met by any combination of the coins.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make the total 0

    # Fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity
    return dp[total] if dp[total] != float('inf') else -1
