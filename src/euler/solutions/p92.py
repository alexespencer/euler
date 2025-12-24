# Seems to be based on p74
def digit_square_sum(n):
    sum = 0

    for c in str(n):
        sum += int(c) ** 2

    return sum


def add_to_chain_lookup(n, chain_cache):
    if n not in chain_cache:
        dssum = digit_square_sum(n)
        chain_cache[n] = dssum
        if dssum not in chain_cache:
            add_to_chain_lookup(dssum, chain_cache)
        return dssum
    else:
        return chain_cache[n]


# Function for length of chain
def chain_length(n, chain_cache):
    numbers_seen = set()
    while n not in numbers_seen:
        numbers_seen.add(n)
        n = add_to_chain_lookup(n, chain_cache)
    return len(numbers_seen), 89 in numbers_seen


def solution() -> int:
    assert digit_square_sum(44) == 32
    assert digit_square_sum(32) == 13

    chain_cache = {}

    count_89 = 0
    for i in range(1, 10**7):
        if chain_length(i, chain_cache)[1]:
            count_89 += 1
    return count_89


if __name__ == "__main__":
    print(solution())
