# How long would it take to iterate?
# For 1 billion, it takes 74 seconds, without any computation - this would take too long
# What about using pythagorian triples? Something we have done before in problem 75
# Our p75 solution, using Euclid's formula, is still not optimal, try again...
from time import time
import sys
import os

sys.path.insert(0, os.getcwd())

from euler import HCF


def pythag_triples(k):  # k is the max length of the hypotenuse
    n, m = 1, 2
    while m * m + 1 < k:
        if n >= m:
            n, m = m % 2, m + 1
        c = m * m + n * n
        if c >= k:
            n = m
            continue
        if HCF(n, m) == 1:
            yield m * m - n * n, 2 * m * n, c
        n += 2


start_time = time()

print("Generating pythag triples...")
max_perimeter = 1000000000
# max_perimeter = 10000000
max_length_side = (max_perimeter // 3) + 2

# For each triple, see if it forms an almost equilateral triangle
almost_equilateral = []

print("Finding almost equilateral triangles...")
for triple in pythag_triples(max_length_side):
    a, b, c = triple
    # If the absolute difference between 2a and c is 1, we have found an AET
    if abs(2 * a - c) == 1:
        print(
            f"Pythag triple {triple} forms an almost equilateral triangle with perimeter {2 * c + 2 * a}, sides = {[c, c, 2 * a]}"
        )
        almost_equilateral.append([c, c, 2 * a])
    if abs(2 * b - c) == 1:
        print(
            f"Pythag triple {triple} forms an almost equilateral triangle with perimeter {2 * c + 2 * b}, sides = {[c, c, 2 * b]}"
        )
        almost_equilateral.append([c, c, 2 * b])

end_time = time()

# Sum the perimeter of all AETs
sum_perimeter = sum([sum(triple) for triple in almost_equilateral])
print(sum_perimeter)

print(f"Time taken: {end_time - start_time} seconds")
