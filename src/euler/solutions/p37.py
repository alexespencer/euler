from euler.primes import prime_sieve


def truncate_set(n: int) -> set[int]:
    numbers = set([n])  # Include n

    str_n = str(n)

    # Truncate digit by digit from left
    for i in range(len(str_n)):
        numbers.add(int(str_n[i:]))

    # Truncate digit by digit from right
    for i in range(len(str_n), 0, -1):
        numbers.add(int(str_n[:i]))

    return numbers


def solution() -> int:
    assert truncate_set(123) == set([123, 12, 1, 23, 3])
    primes = set(prime_sieve(1_000_000))

    truncatable_primes = set()

    for prime in primes:
        if prime > 9 and all(x in primes for x in truncate_set(prime)):
            truncatable_primes.add(prime)

    assert len(truncatable_primes) == 11

    return sum(truncatable_primes)


if __name__ == "__main__":
    print(solution())
