import sys, os
print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import is_prime
from itertools import islice

from datetime import datetime

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

print("Finding primes under 1,000,000...", end='')
primes_1m = [2] + [x for x in range(3, 1000001, 2) if is_prime(x)]
print("done")

# Function to give a sliding window
def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def method1(window_size):
    for w in window(primes_1m, window_size):
        if w[-1] >= 500000:
            print(f"Aborting checking window size {window_size} as largest prime is now >= 500,000")
            return None

        sum_window = sum(w)

        if sum_window >= 1000000:
            print(f"Aborting checking window size {window_size} as sum of the window is now >= 1,000,000")
            return None

        if sum_window in primes_1m:
            print(window_size, sum_window, w)
            return True

overall_start = datetime.now()
# Take a sliding window of 6 and see if it adds to a prime
for window_size in range(1000, 21, -1):
    start_time = datetime.now()
    found = method1(window_size)

    end_time = datetime.now()
    print("Time taken:", end_time - start_time)
    if found:
        break
overall_end = datetime.now()
print("Total taken:", overall_end - overall_start)