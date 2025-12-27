from euler import find_factors
from euler.primes import is_prime


def solution() -> int:
    factors = find_factors(600851475143)
    return max(f for f in factors if is_prime(f))


if __name__ == "__main__":
    print(solution())
