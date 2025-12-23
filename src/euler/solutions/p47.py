from euler.primes import prime_factors

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# Use a "shortcircuit", if we get a prime factor already in the list, reset and use this number as the "start" of the 4 numbers


def solution() -> int:
    # Find the first number with 4 prime factors
    n = 2
    while len(prime_factors(n)) < 4:
        n += 1

    print("First number with 4 prime factors is:")
    print(n, ", with prime factors of", prime_factors(n))

    # But we can be a bit smarter, and jump straight to the lowest number were there are 4 contigous numbers with 4 prime factors
    n = 2
    count_contigous = 0
    first_number = n
    while count_contigous < 4:
        if len(prime_factors(n)) == 4:
            count_contigous += 1
            if count_contigous == 1:
                first_number = n
        else:
            count_contigous = 0
            first_number = n
        n += 1

    return first_number


if __name__ == "__main__":
    print(solution())
