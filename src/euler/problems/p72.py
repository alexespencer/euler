# This one looks familiar...and seems to need us to discover (or determine) the number of possible fractions. Let's see if there is a pattern


def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n + 1):
        phi_set[i] = i

    for i in range(2, n + 1):
        if phi_set[i] == i:
            for j in range(i, n + 1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set


def count_possible_fractions(max_d):
    # We can just sum phi(d) for 2 to max_d
    phi_set = phi_1_to_n(max_d)
    return sum(phi_set.values()) - 1


def solution() -> int:
    return count_possible_fractions(10**6)


if __name__ == "__main__":
    print(solution())
