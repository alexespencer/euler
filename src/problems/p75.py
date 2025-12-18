import sys
import os

sys.path.insert(0, os.getcwd())

from euler import generate_pythag_triples

# For a right angled triangle with integer sides there are a number of properties we might be able to use:
# ((a * b) / 2) % 6 == 9
# a * b * c % 60 == 0
# Or...we can use Euclid's formula, but with the k parameter modification so that ALL triples are generated
# ...where m, n, k are positive integers, and m > n and m,n are coprime (HCF(m,n) == 1) and both not odd

max_length = 1500000
triangles = generate_pythag_triples(max_length)

# How many with only one triangle up to the max_length
answer = len([1 for l, t in triangles.items() if len(t) == 1 and l <= max_length])
assert answer == 161667
print(f"Number of Lengths with 1 unique solution (L <= {max_length:,}): {answer}")

# Print the longest PT
longest = max(triangles.keys())
print(f"Longest length {longest}. EG: {list(triangles[longest])[0]}")
