import math
from math import sqrt


def phi(n):
    # Using the prime factorization of n, find the number of relative primes
    # Used the function from https://cp-algorithms.com/algebra/phi-function.html#properties
    # which runs in O(sqrt(n)) time - good enough for me for now
    pfn = prime_factors(n)

    # Turn the prime factors dict into a list and apply function
    pfl = [1 - (1 / pf) for pf in pfn.keys()]

    # Apply function
    return round(n * math.prod(pfl))


def is_prime(n):
    """Returns if a number is prime"""
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n + 1) + 1), 2):
        # for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime_sieve(n):
    n = n + 1
    size = n // 2
    sieve = [1] * size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val :: val] = [0] * tmp
    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]


def prime_factors(n):
    """Returns a dictionary of prime: order. For example 100 (prime factors 2x2x5x5) would return {2: 2, 5:2}"""
    if n == 1:
        return {}

    p = 2
    factors = {}
    while n >= p * p:
        if n % p == 0:
            factors.setdefault(p, 0)
            factors[p] += 1
            n = n // p
        else:
            if p <= 2:
                p += 1
            else:
                p += 2

    n = int(n)
    factors.setdefault(n, 0)
    factors[n] += 1

    return factors
