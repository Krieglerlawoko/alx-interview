#!/usr/bin/python3
"""
Module defining the is_winner function for the prime game.
"""


def is_winner(x, nums):
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
            ben_wins_count += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]
            is_maria_turn = not is_maria_turn

    if maria_wins_count > ben_wins_count:
        return "Winner: Maria"
    elif ben_wins_count > maria_wins_count:
        return "Winner: Ben"
    else:
        return None


def is_prime(n):
    """
    Checks if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return
