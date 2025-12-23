import math


def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n + 1):
        phi_set[i] = i

    for i in range(2, n + 1):
        if phi_set[i] == i:
            for j in range(i, n + 1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set


def is_perm(a, b):
    # Check if two numbers are permutations of each other
    return sorted(str(a)) == sorted(str(b))


def solution() -> int:
    assert phi_1_to_n(10) == {
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 4,
        6: 2,
        7: 6,
        8: 4,
        9: 6,
        10: 4,
    }

    # Find the value of n, 1 < n < 10 ** 7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum
    min_ratio_found = math.inf
    min_found_at_n = 0
    n_max = 10**7
    phi_set = phi_1_to_n(n_max)
    del phi_set[1]
    for n, phi_value in phi_set.items():
        ratio = n / phi_value
        if ratio < min_ratio_found and is_perm(n, phi_value):
            min_ratio_found = ratio
            min_found_at_n = n

    return min_found_at_n


if __name__ == "__main__":
    print(solution())
