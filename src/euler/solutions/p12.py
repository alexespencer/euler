from math import prod

from euler import find_factors
from euler.primes import prime_factors


def number_factors(n):
    pf = prime_factors(n)
    return prod([ex + 1 for ex in pf.values()])


def first_triangle_number_with_over_n_factors(n, factor_count_lookup):
    # Find the first key greater than or equal to n
    key = min([k for k in factor_count_lookup.keys() if k >= n])

    return factor_count_lookup[key]


def solution() -> int:
    for i in range(1, 1000):
        assert number_factors(i) == len(find_factors(i))

    factor_count_lookup = {
        0: 1,
        1: 3,
    }  # key: n value = value of the FIRST triangle number with OVER the n (key) factors

    # What's the first number with 10 ** 3 divisors?
    # The first number with OVER 10**3 factors is 842161320. It is the 41040th triangle number and has 1024 factors
    # The "first numbers" with over N factors are always even (after the first 2 triangle numbers). This means we can
    # reduce the numbers we search by skipping over odd triangle numbers. The pattern is [odd, odd, even even]
    limit = 10**3
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

    assert first_triangle_number_with_over_n_factors(5, factor_count_lookup) == 28
    value = first_triangle_number_with_over_n_factors(500, factor_count_lookup)
    return value


if __name__ == "__main__":
    print(solution())
