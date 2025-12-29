from euler import is_prime


def quadratic_consecutive_prime_count(a: int, b: int) -> int:
    """Returns how many consecutive primes (N) a quadratic in the form n**2 + n*a + b creates"""
    n = 0
    while True:
        x = n**2 + (n * a) + b
        if x < 0 or not is_prime(x):
            return n
        n += 1


def solution() -> int:
    assert quadratic_consecutive_prime_count(1, 41) == 40
    assert quadratic_consecutive_prime_count(-79, 1601) == 80

    ab_count = {}
    for a in range(-999, 1000):
        for b in range(-1000, 1000 + 1):
            ab_count[(a, b)] = quadratic_consecutive_prime_count(a, b)

    # Find (a, b) that has the max number of primes
    a, b = max(ab_count, key=lambda k: ab_count[k])
    return a * b


if __name__ == "__main__":
    print(solution())
