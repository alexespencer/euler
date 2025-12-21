def totient_maximum(L, primes):
    n = 1

    for i in primes:
        # exit the loop if if product is now greater than the limit
        if n * i > L:
            return n

        # if product is less than the limit multiply the prime with the previous
        # value of n and store in n
        n = n * i

    raise ValueError("Not enough primes")


# Prime multiplication...
def solution() -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31]

    return totient_maximum(1000000, primes)


if __name__ == "__main__":
    print(solution())
