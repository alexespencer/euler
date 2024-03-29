# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt, prod
from functools import reduce
from datetime import datetime

def find_factors(n):
    """Returns the factors of n (must be an int)"""
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

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
            n = n / p
        else:
            if p <= 2:
                p += 1
            else:
                p += 2

    n = int(n)
    factors.setdefault(n, 0)
    factors[n] += 1

    return factors

def number_factors(n):
    pf = prime_factors(n)
    return prod([ex+1 for ex in pf.values()])

for i in range(1, 1000):
    assert number_factors(i) == len(find_factors(i))

factor_count_lookup = {0: 1,
                       1: 3} # key: n value = value of the FIRST triangle number with OVER the n (key) factors

# start_time = datetime.now()
# for i in range(5000):
#     f = len(find_factors(842161320))
# print(f)
# print(f"Time taken: {datetime.now() - start_time}")

# start_time = datetime.now()
# for i in range(500):
#     x = number_factors(842161320)
# print(x)

# print(f"Time taken: {datetime.now() - start_time}")
# exit()
# What's the first number with 10 ** 3 divisors?
# The first number with OVER 10**3 factors is 842161320. It is the 41040th triangle number and has 1024 factors
# The "first numbers" with over N factors are always even (after the first 2 triangle numbers). This means we can
# reduce the numbers we search by skipping over odd triangle numbers. The pattern is [odd, odd, even even]
limit = 10 ** 3
sum = 6
i = 3
keep_going = True
max_factors_found = 2
while keep_going:
    for _ in range(2):
        
        num_factors = number_factors(sum)
        if num_factors > max_factors_found:
            max_factors_found = num_factors
            key = num_factors - 1
            factor_count_lookup[key] = sum
        
            if num_factors > limit:
                keep_going = False
                break
        
        i += 1
        sum += i

    for _ in range(2):
        i += 1
        sum += i

for k, v in factor_count_lookup.items():
    print(k, v)
    
def first_triangle_number_with_over_n_factors(n):
    # Find the first key greater than or equal to n
    key = min([k for k in factor_count_lookup.keys() if k >= n])
    
    return factor_count_lookup[key]

assert first_triangle_number_with_over_n_factors(5) == 28
assert first_triangle_number_with_over_n_factors(500) == 76576500