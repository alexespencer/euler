from itertools import islice

from euler import is_prime

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


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


def method1(window_size, primes_1m: list[int]) -> int | None:
    for w in window(primes_1m, window_size):
        if w[-1] >= 500000:
            return None

        sum_window = sum(w)

        if sum_window >= 1000000:
            return None

        if sum_window in primes_1m:
            return sum_window


def solution() -> int:
    primes_1m = [2] + [x for x in range(3, 1000001, 2) if is_prime(x)]

    # Take a sliding window of 6 and see if it adds to a prime
    for window_size in range(1000, 21, -1):
        value = method1(window_size, primes_1m)
        if value is not None:
            return value

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solution())
