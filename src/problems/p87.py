import os
import sys

sys.path.insert(0, os.getcwd())

from euler import is_prime

# Max prime for 1st element would be root(50,000,000 - 24): <= 7071
# Max prime for 2nd element would be cuberoot(50,000,000 - 20): <= 368
# Max prime for 3rd element would be quadroot(50,000,000 - 16): <= 84

all_choices = []
limit = 50000000

for p in range(2, 5):
    choices = []

    choices.append(2**p)

    for i in range(3, int(limit ** (1 / p)) + 1, 2):
        if is_prime(i):
            choices.append(i**p)

    all_choices.append(choices)

unique_solutions = [
    n1 + n2 + n3
    for n1 in all_choices[0]
    for n2 in all_choices[1]
    for n3 in all_choices[2]
    if n1 + n2 + n3 < limit
]

unique_solutions = set(unique_solutions)

print(f"Number of solutions for limit of {limit} is {len(unique_solutions)}")
