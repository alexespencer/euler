from euler.primes import prime_sieve


def solution() -> int:
    n = 10001

    guess = n * 10
    while True:
        # Generate at least n primes
        primes = prime_sieve(guess)
        if len(primes) < n:
            guess *= 2
        else:
            break

    return primes[n - 1]


if __name__ == "__main__":
    print(solution())
