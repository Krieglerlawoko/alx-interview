#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    if x < 1 or not nums:
        return None
    mariaswins, benswins = 0, 0
    # generate primes with a limit of the maximum number in nums
    a = max(nums)
    primes = [True for _ in range(1, a + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, a in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: a])))
        benswins += primes_count % 2 == 0
        mariaswins += primes_count % 2 == 1
    if mariaswins == benswins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
