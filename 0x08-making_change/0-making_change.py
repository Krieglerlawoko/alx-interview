#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make the total 0

    # Fill the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinit
    return dp[total] if dp[total] != float('inf') else -1
