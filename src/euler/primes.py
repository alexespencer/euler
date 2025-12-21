import math

from euler import prime_factors


def phi(n):
    # Using the prime factorization of n, find the number of relative primes
    # Used the function from https://cp-algorithms.com/algebra/phi-function.html#properties
    # which runs in O(sqrt(n)) time - good enough for me for now
    pfn = prime_factors(n)

    # Turn the prime factors dict into a list and apply function
    pfl = [1 - (1 / pf) for pf in pfn.keys()]

    # Apply function
    return round(n * math.prod(pfl))
