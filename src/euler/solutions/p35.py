from euler.primes import prime_sieve


def number_rotations(n: int) -> list[int]:
    """Returns all the rotations of n, including n itself
    i.e. number_rotations(123) returns [123, 231, 312]"""
    str_n = str(n)

    return [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]


def solution() -> int:
    primes = set(prime_sieve(1_000_000 + 1))
    assert number_rotations(197) == [197, 971, 719]

    count = 0
    for prime in primes:
        if all(rotation in primes for rotation in number_rotations(prime)):
            count += 1

    return count


if __name__ == "__main__":
    print(solution())
