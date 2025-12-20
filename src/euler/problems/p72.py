import os
import sys
import time

sys.path.insert(0, os.getcwd())

from euler import HCF, find_factors

# This one looks familiar...and seems to need us to discover (or determine) the number of possible fractions. Let's see if there is a pattern


def reduce_fraction(numerator, denominator):
    # Reduce the fraction to lowest terms
    while True:
        cd = HCF(numerator, denominator)
        if cd == 1:
            break

        numerator = numerator // cd
        denominator = denominator // cd
    return numerator, denominator


assert reduce_fraction(10, 20) == (1, 2)
assert reduce_fraction(4, 8) == (1, 2)
assert reduce_fraction(3, 7) == (3, 7)
assert reduce_fraction(3 * 15 * 10 * 3 * 19, 7 * 15 * 10 * 3 * 19) == (3, 7)


def count_possible_fractions_slow(max_d):
    # Generate fractions up to the max_fraction...this is VERY SLOW
    possible_fractions = []

    for n in range(1, max_d + 1):
        for d in range(n + 1, max_d + 1):
            if n / d < 1:
                rf = reduce_fraction(n, d)
                if rf not in possible_fractions:
                    possible_fractions.append(rf)

    return len(possible_fractions)


assert count_possible_fractions_slow(8) == 21


def non_contributing(d, common_factors):
    ncfs = []
    for f in common_factors:
        ncfs.extend([i for i in range(f, d, f)])

    return len(set(ncfs))


# Proud of this, but it's still too slow
def count_possible_fractions(max_d):
    count_fractions = 0
    covered_factors = set()

    for d in range(max_d, 1, -1):
        # Display some form of progress
        if d % 10000 == 0:
            print(d)

        # If we've seen this denominator as a previous factor, it will not contribute to any fractions
        if d in covered_factors:
            continue

        # Find the factors of the denominator (good job we sped this up)
        factors = find_factors(d)

        # Factors in common with covered factors
        common_factors = set(factors) & set(covered_factors)

        # If no shared factors, contribute the max
        if not common_factors:
            count_fractions += d - 1
        else:
            # Otherwise, we need to remove any that divide into any of the common factors

            # contributing_fractions = [1 for i in range(1, d) if not any(i % (d // f) == 0 for f in common_factors)]
            # count_fractions += sum(contributing_fractions)
            count_fractions += (
                d - 1 - non_contributing(d, [d // f for f in common_factors])
            )

        # Now update the covered factors
        new_covered_factors = {f for f in factors if f != 1 and f != d}
        covered_factors.update(new_covered_factors)

    return count_fractions


def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n + 1):
        phi_set[i] = i

    for i in range(2, n + 1):
        if phi_set[i] == i:
            for j in range(i, n + 1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set


def count_possible_fractions_fast(max_d):
    # We can just sum phi(d) for 2 to max_d
    phi_set = phi_1_to_n(max_d)
    return sum(phi_set.values()) - 1


if True:
    print("Running tests")
    for i in range(10, 105):
        assert count_possible_fractions(i) == count_possible_fractions_slow(i)
        assert count_possible_fractions_fast(i) == count_possible_fractions_slow(i)

    assert non_contributing(12, [3, 4, 6]) == 5
    assert non_contributing(10, [2, 5]) == 5
    print("Tests complete")

if False:
    starttime = time.time()
    print(count_possible_fractions(10**6))
    # count_possible_fractions(10**4)
    endtime = time.time()
    print(f"Time taken: {endtime - starttime}")

# Old way took 17000 seconds, this way takes 1.3 seconds!
starttime = time.time()
print(count_possible_fractions_fast(10**6))
# count_possible_fractions(10**4)
endtime = time.time()
print(f"Time taken: {endtime - starttime}")
