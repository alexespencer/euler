# Doing it by hand for the first 7 numbers, we get (from 0) 0, 1, 2, 4, 6, 10, 14 which looks like the OEIS sequence A000123,
# however it could also be +1, which is 2, 3, 5, 7, 11, 15 which is the OEIS sequence A000041 - this looks like the correct solution as the p(8) for A000123 does not equal 20, but p(8) for A000041 does equal 21
import time


def accel_asc_count(n):
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
            yield 1
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield 1


def number_ways(n):
    return len(list(accel_asc_count(n))) - 1


assert number_ways(5) == 6
assert number_ways(7) == 14

starttime = time.time()
print(number_ways(100))
endtime = time.time()
print(f"Time taken: {endtime - starttime}")
