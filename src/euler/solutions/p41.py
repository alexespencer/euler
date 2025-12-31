from euler.primes import prime_sieve


def is_pandigital(n: int) -> bool:
    max_digit = len(str(n))
    if len(str(n)) > 9:
        return False
    return set(str(n)) == set(map(str, range(1, max_digit + 1)))


def solution() -> int:
    assert is_pandigital(1234) is True
    assert is_pandigital(12355) is False

    # Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
    # Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
    primes = prime_sieve(10**7 - 1)

    return max(prime for prime in primes if is_pandigital(prime))


if __name__ == "__main__":
    print(solution())
