#!/usr/bin/python3
"""
Determine the minimum number of coins to make a given amount
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of integers representing coin denominations.
        total (int): Target amount.

    Returns:
        int: Minimum number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    #dp array initialized where dp[x] is the minimum coins needed for amount x
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed for total 0

    # dp array populated
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
