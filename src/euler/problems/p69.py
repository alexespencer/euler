import math

from euler import find_factors


def get_factor_set(n, factor_sets):
    if n not in factor_sets:
        factor_sets[n] = set(find_factors(n))
    return factor_sets[n]


def phi(n, factor_sets, limit=math.inf):
    # How many relative primes does n have
    # two numbers are relatively prime if they share no common positive factors (Except 1)
    factors_n = get_factor_set(n, factor_sets)

    found = 1
    for i in range(2, n):
        if get_factor_set(i, factor_sets).intersection(factors_n) == {1}:
            found += 1

        if found > limit:
            return math.inf

    return found


def totient_maximum(L, primes):
    n = 1

    for i in primes:
        # exit the loop if if product is now greater than the limit
        if n * i > L:
            return n

        # if product is less than the limit multiply the prime with the previous
        # value of n and store in n
        n = n * i

    raise ValueError("Not enough primes")


# Prime multiplication...
def solution() -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31]

    return totient_maximum(1000000, primes)


if __name__ == "__main__":
    print(solution())
