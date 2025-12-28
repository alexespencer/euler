from euler import find_factors


def d(n: int) -> int:
    return sum(find_factors(n)) - n


def solution() -> int:
    assert d(220) == 284
    assert d(284) == 220
    # Find d(n) for 1..10_000
    n_to_dn_map = {}
    for n in range(1, 10_000):
        n_to_dn_map[n] = d(n)

    # Number is amicable if d(a) == b and d(b) == a
    amicable_numbers = set()
    for n, dn in n_to_dn_map.items():
        if dn != n and dn in n_to_dn_map and n_to_dn_map[dn] == n:
            amicable_numbers.add(n)
            amicable_numbers.add(dn)

    return sum(amicable_numbers)


if __name__ == "__main__":
    print(solution())
