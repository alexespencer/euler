import sys
import os

sys.path.insert(0, os.getcwd())

from euler import HCF

# Test speed of our HCF function
# start = time.time()
# for a in range(1, 10 ** 4):
#     for b in range(1, 10 ** 4):
#         HCF(a, b)
# end = time.time()
# print("HCF function took", end - start, "seconds")

min_fraction = 2 / 7
max_fraction = 1


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

# Generate fractions up to the max_fraction...this is VERY SLOW
possible_fractions = []
for n in range(1, 8 + 1):
    for d in range(1, 8 + 1):
        if n / d < max_fraction:
            rf = reduce_fraction(n, d)
            if rf not in possible_fractions:
                possible_fractions.append(rf)

# # Sort possible fractions by their numeric value
possible_fractions = sorted(possible_fractions, key=lambda x: x[0] / x[1])
print(possible_fractions)
print([n / d for n, d in possible_fractions])
# print(possible_fractions[possible_fractions.index((3, 7))-5:possible_fractions.index((3, 7))+10])

# Sometimes...thinking about it and doing it by hand is best!
# The "smallest" amount you can take off of 3/7 is 1/1,000,000 = so just need to work out what factor to times 3/7 by
f = 1000000 // 7
n = 3 * f - 1
d = f * 7
print(reduce_fraction(n, d))
