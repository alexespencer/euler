import os
import sys

print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import is_prime

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#  (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

# Starting from n 1000 as the first number, we need to find an x that:
# n + x + x <= 9973 (the largest prime below 9999)

# Where the digits of n are permuted to form n + x and n + x + x AND n, n + x and n + x + x are all prime


def check_permutations(number_list):
    # For each number in the list, convert to a sorted array. If there is only one unique sorted list, then they are permutations
    list_set = {"".join(sorted(list(str(number)))) for number in number_list}
    if len(list_set) == 1:
        return True

    return False


assert check_permutations([1487, 4817, 8147])
assert check_permutations([123, 321])
assert not check_permutations([123, 31])
assert not check_permutations([123, 31, 321])

for n1 in range(1000, 9974):
    if not is_prime(n1):
        continue

    # Determine our max x
    max_x = int((9973 - n1) / 2) + 1

    for x in range(1, max_x):
        n2, n3 = n1 + x, n1 + x + x
        if is_prime(n2) and is_prime(n3):
            # Check the permutations
            if check_permutations([n1, n2, n3]):
                print(n1, n2, n3)
                break
