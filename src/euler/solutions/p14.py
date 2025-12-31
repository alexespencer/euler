def seq(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def longest_collatz(n, collatz_length):
    if n == 1:
        return 1
    elif n in collatz_length:
        return collatz_length[n]
    else:
        length = 1 + longest_collatz(seq(n), collatz_length)
        collatz_length[n] = length

        return length


def longest_less_n(n, n_to_length_lookup):
    # Find the largest key in n_to_length_lookup that is less than or equal to n
    key = max([k for k in n_to_length_lookup if k <= n])

    # Now, find the max of the length_to_n_lookup[val for the key in n_to_length_lookup]
    return max(n_to_length_lookup[key][1])


def solution() -> int:
    collatz_length = {}

    assert longest_collatz(1, collatz_length) == 1
    assert longest_collatz(2, collatz_length) == 2
    assert longest_collatz(4, collatz_length) == 3
    assert longest_collatz(8, collatz_length) == 4
    assert longest_collatz(13, collatz_length) == 10

    n_to_length_lookup = {}

    longest_chain = 0
    for i in range(1, 1000000):
        length = longest_collatz(i, collatz_length)
        if length >= longest_chain:
            longest_chain = length
            n_to_length_lookup.setdefault(i, [0, set()])
            n_to_length_lookup[i][0] = length
            n_to_length_lookup[i][1].add(i)

    assert longest_less_n(1000000, n_to_length_lookup) == 837799
    return longest_less_n(1000000, n_to_length_lookup)


if __name__ == "__main__":
    print(solution())
