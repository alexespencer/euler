import os
import sys
import time

sys.path.insert(0, os.getcwd())

from euler import is_prime


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        L = k + 1
        while x <= y:
            a[k] = x
            a[L] = y
            yield a[: k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[: k + 1]


def count_primes(n, show_ways=False):
    ways = list(accel_asc(n))
    count_prime = 0
    for way in ways:
        if all(is_prime(i) for i in way) and len(way) > 1:
            if show_ways:
                print(way)
            count_prime += 1

    return count_prime


assert count_primes(10) == 5

starttime = time.time()
n = 10
while True:
    cp = count_primes(n)
    if cp > 5000:
        print(f"The number {n} can be written as the sum of {cp} primes")
        break
    n += 1
endtime = time.time()
print(f"Time taken: {endtime - starttime}")

# count_primes(n, show_ways=True)
