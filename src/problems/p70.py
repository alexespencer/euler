import os
import sys
import time

sys.path.insert(0, os.getcwd())

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


def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n + 1):
        phi_set[i] = i

    for i in range(2, n + 1):
        if phi_set[i] == i:
            for j in range(i, n + 1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set


def is_perm(a, b):
    # Check if two numbers are permutations of each other
    return sorted(str(a)) == sorted(str(b))


assert phi(2) == 1
assert phi(3) == 2
assert phi(4) == 2
assert phi(5) == 4
assert phi(6) == 2
assert phi(7) == 6
assert phi(8) == 4
assert phi(9) == 6
assert phi(10) == 4
assert phi(87109) == 79180

assert phi_1_to_n(10) == {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4, 9: 6, 10: 4}

# Find the value of n, 1 < n < 10 ** 7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum
# Even this is too slow! Is it the checking of perms of Phi? Not really, phi itself is too slow
# Try the better function
starttime = time.time()
min_ratio_found = math.inf
n_max = 10**7
phi_set = phi_1_to_n(n_max)
del phi_set[1]
for n, phi_value in phi_set.items():
    if is_perm(n, phi_value):
        ratio = n / phi_value
        if ratio < min_ratio_found:
            min_ratio_found = ratio
            print("new min ratio", min_ratio_found, "at n", n)

endtime = time.time()
print("Time taken:", str(endtime - starttime))
