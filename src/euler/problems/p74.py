from math import factorial


def digit_factorial_sum(n, factorial_cache):
    sum = 0

    for c in str(n):
        sum += factorial_cache[c]

    return sum


def add_to_chain_lookup(n, chain_lookup, factorial_cache):
    dfs = digit_factorial_sum(n, factorial_cache)
    if n not in chain_lookup:
        chain_lookup[n] = dfs
        if dfs not in chain_lookup:
            add_to_chain_lookup(dfs, chain_lookup, factorial_cache)


# Function for length of chain
def chain_length(n, chain_lookup):
    numbers_seen = []
    while n not in numbers_seen:
        numbers_seen.append(n)
        n = chain_lookup[n]
    return len(numbers_seen)


def solution() -> int:
    factorial_cache = {}
    for i in range(0, 10):
        factorial_cache[str(i)] = factorial(i)
    assert digit_factorial_sum(145, factorial_cache) == 145
    assert digit_factorial_sum(69, factorial_cache) == 363600

    # Chain lookup
    chain_lookup = {}

    for i in range(1, 10**6):
        add_to_chain_lookup(i, chain_lookup, factorial_cache)

    # Count how many numbers <= 10**6 have a chain length of exactly 60
    # We could make this faster by caching the chain length of each sub chain - so if the number is encountered again, we can skip the rest of the chain
    count = 0
    for i in range(1, 10**6):
        if chain_length(i, chain_lookup) == 60:
            count += 1

    return count


if __name__ == "__main__":
    print(solution())
