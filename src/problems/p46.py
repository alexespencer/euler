import os
import sys

print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import is_composite_number, is_prime

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# Prepopulate primes up to 1000
prime_limit = 6000
primes = set([2] + [n for n in range(3, prime_limit, 2) if is_prime(n)])

# Prepopulate twice of squares up to 1000
twice_squares = [2 * n * n for n in range(1, 1000) if 2 * n * n < prime_limit]


def goldbach(n):
    # Find a match out of the choices we have
    ts_choices = [x for x in twice_squares if x < n - 2]

    for ts in ts_choices:
        # Is the difference a prime
        if n - ts in primes:
            return True

    return False


for gold in range(33, 10000, 2):
    if is_composite_number(gold) and not goldbach(gold):
        print(gold)
        if gold >= prime_limit:
            print("WARNING - below prime limit - raise the prime limit to be sure")
        break
