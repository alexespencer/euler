import sys, os
sys.path.insert(0, os.getcwd())

from euler import find_factors
import math

factor_sets = {}

def get_factor_set(n):
    if n not in factor_sets:
        factor_sets[n] = set(find_factors(n))
    return factor_sets[n]

def phi(n, limit=math.inf):
    # How many relative primes does n have
    # two numbers are relatively prime if they share no common positive factors (Except 1)
    factors_n = get_factor_set(n)

    found = 1
    for i in range(2, n):
        if get_factor_set(i).intersection(factors_n) == {1}:
            found += 1

        if found > limit:
            return math.inf

    return found

assert phi(2) == 1
assert phi(3) == 2
assert phi(4) == 2
assert phi(5) == 4
assert phi(6) == 2
assert phi(7) == 6
assert phi(8) == 4
assert phi(9) == 6
assert phi(10) == 4

# This is too slow, even with caching of factors
# max_n = 1000000
# max_n_over_phi_n = 0
# n_at_max = None
# for n in range(20, max_n+1, 10):
#     # If phi ever gets to be over n / current max it can't be the new max
#     limit = int(n / max_n_over_phi_n) + 1 if max_n_over_phi_n else math.inf

#     n_over_phi_n = n / phi(n, limit)


#     if n_over_phi_n > max_n_over_phi_n:
#         max_n_over_phi_n = n_over_phi_n
#         n_at_max = n
#         print("new max at n", n)

#     if n % 10000 == 0:
#         print("n", n)

# print(n_at_max, max_n_over_phi_n)

# Different technique, prime multiplication

# variable primes stores list of primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31]

def totient_maximum(L):
    n = 1

    for i in primes:
        # exit the loop if if product is now greater than the limit
        if n * i > L:
            return n

        # if product is less than the limit multiply the prime with the previous
        # value of n and store in n
        n = n * i

    raise ValueError("Not enough primes")

print(f"The totient maximum of N <= 1,000,000 is", totient_maximum(1000000))