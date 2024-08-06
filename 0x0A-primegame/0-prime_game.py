#!/usr/bin/python3
"""
Prime game module.
"""


def sieve(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, n + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    if not nums or x <= 0:
        return None
    max_num = max(nums)
    primes = sieve(max_num)
    prime_set = set(primes)

    def game_outcome(n):
        # Tracks moves made in a set
        moves = [0] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            for multiple in range(prime, n + 1, prime):
                moves[multiple] += 1
        return moves

    # Determines the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        moves = game_outcome(n)
        # If the number of prime moves is even, Ben wins (because Maria starts)
        if sum(moves) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
