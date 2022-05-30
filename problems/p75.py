import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import HCF

triangles = {}

# For a right angled triangle with integer sides there are a number of properties we might be able to use:
# ((a * b) / 2) % 6 == 9
# a * b * c % 60 == 0
# Or...we can use Euclid's formulate, but with the k parameter modification so that ALL triples are generated
# ...where m, n, k are positive integers, and m > n and m,n are coprime (HCF(m,n) == 1) and both not odd

def generate_pythag_triples(m, n, max_length):
    triples = []

    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    k = 1
    while True:
        if (k * a) + (k * b) + (k * c) > max_length:
            break

        triples.append(tuple(sorted([k * a, k * b, k * c])))
        k += 1

    return triples

max_length = 1500000

# What is the max value of m we need to use?
m = 2
while True:
    if generate_pythag_triples(m, 1, max_length):
        m += 1
    else:
        break

# Generate all triangles up to our max length
max_m = m * 2
triangles = {}
for m in range(2, max_m):  
    # If m is odd then n cannot also be odd we we get to skip every other n
    step = 1 if m % 2 == 0 else 2
    for n in range(step, m, step):
        if HCF(m, n) == 1:
            for triple in generate_pythag_triples(m, n, max_length):
                length = sum(triple)
                triangles.setdefault(length, []).append(triple)

# Sometimes we can generate things like (12, 16, 20), (12, 16, 20) - from different m/n pairs - so make them unique now
for length, triples in triangles.items():
    triangles[length] = set(triples)

# Run tests (from wiki, all of these are expected to be found)
pt_100 = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
        (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
        (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
        (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]

for triple in pt_100:
    assert triple in triangles[sum(triple)]

# How many with only one triangle up to the max_length
print(f"Number of Lengths with 1 unique solution (L <= {max_length:,}): {len([1 for l, t in triangles.items() if len(t) == 1 and l <= max_length])}")
