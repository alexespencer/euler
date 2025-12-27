from euler.primes import prime_sieve


def solution() -> int:
    primes = prime_sieve(2_000_000)
    return sum(primes)


if __name__ == "__main__":
    print(solution())
