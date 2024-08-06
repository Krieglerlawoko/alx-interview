#!/usr/bin/python3
"""
Module defining the is_winner function for the prime game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the end number for each round.

    Returns:
    str: The winner of the game, either
    "Maria" or "Ben". Returns None if it's a tie.
    """
    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        rounds_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        if not primes_set:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while(True):
            if not primes_set:
                if isMariaTurns:
                    benWinsCount += 1
                else:
                    mariaWinsCount += 1
                break

            smallestPrime = primes_set.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """
    Generates a list of prime numbers in a given range.

    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    list: A list of prime numbers within the range.
    """
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes
