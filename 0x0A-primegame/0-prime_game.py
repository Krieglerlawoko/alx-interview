#!/usr/bin/python3
"""
Prime game module.
"""


def is_winner(x, nums):
    """
    Determines the winner of a prime game session with `x` rounds.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the end number for each round.

    Returns:
    str: The winner of the game, either
    "Maria" or "Ben". Returns None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Filter the number of primes less than or equal
    for num in nums:
        primes_count = sum(primes[0:num + 1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
