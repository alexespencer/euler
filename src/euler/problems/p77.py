from euler.primes import is_prime


# NOTE: this could be re-used in p76 but
# the extra computation required to yield
# the number instead of just counting nearly
# doubles the compute time
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


def solution() -> int:
    assert count_primes(10) == 5

    n = 10
    while True:
        cp = count_primes(n)
        if cp > 5000:
            return n
        n += 1


if __name__ == "__main__":
    print(solution())
