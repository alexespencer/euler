# log (3 ** 125) == 125 * log(3)

from math import log
from tqdm import tqdm

# Read in the data (data/p99/txt) which has lines of data in the form of "base,exponent"
with open("data/p99.txt", "r") as f:
    base_exp = f.read().splitlines()

# Convert to a list of tuples
base_exp = [tuple(map(int, line.split(","))) for line in base_exp]

largest_number = 0
largest_line = 0
for line_number, (base, exponent) in tqdm(enumerate(base_exp)):
    n = exponent * log(base)
    if n > largest_number:
        largest_number = n
        largest_line = line_number

print(largest_line + 1)
print(largest_number)
