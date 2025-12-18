import sys
import os

print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import prime_factors

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# Use a "shortcircuit", if we get a prime factor already in the list, reset and use this number as the "start" of the 4 numbers

# Find the first number with 4 prime factors
n = 2
while len(prime_factors(n)) < 4:
    n += 1

print("First number with 4 prime factors is:")
print(n, ", with prime factors of", prime_factors(n))

# But we can be a bit smarter, and jump straight to the lowest number were there are 4 contigous numbers with 4 prime factors
n = 2
count_contigous = 0
while count_contigous < 4:
    if len(prime_factors(n)) == 4:
        count_contigous += 1
        if count_contigous == 1:
            first_number = n
    else:
        count_contigous = 0
        first_number = 0
    n += 1

print("First number where the next 4 numbers have 4 prime factors is:", first_number)
n = first_number

# [(i, i+len(b)) for i in range(len(a)) if a[i:i+len(b)] == b]

# Set this as our current lowest number, and keep track of its prime factors
lowest_number = n
current_number = n
current_prime_factors = [f"{k}^{v}" for k, v in prime_factors(current_number).items()]
consecutive_count = 1
history = [(current_number, prime_factors(current_number))]

while consecutive_count < 4:
    # Check the next number
    next_prime_factors = prime_factors(current_number + 1)

    # Check if any are repeats
    if len(next_prime_factors) != 4:
        # Reset
        current_number = current_number + 1
        lowest_number = current_number + 1

        consecutive_count = 0
        current_prime_factors = []

        history = []
    elif any(
        [f"{k}^{v}" in current_prime_factors for k, v in next_prime_factors.items()]
    ):
        # Reset
        current_number = current_number + 1
        lowest_number = current_number + 1

        consecutive_count = 1
        current_prime_factors = [f"{k}^{v}" for k, v in next_prime_factors.items()]

        history = [(current_number, next_prime_factors)]
    else:
        # Add
        current_number = current_number + 1  # (leave lowest number alone)
        consecutive_count += 1
        current_prime_factors.extend(
            [f"{k}^{v}" for k, v in next_prime_factors.items()]
        )

        history.append((current_number, next_prime_factors))

print(lowest_number)
print(history)
