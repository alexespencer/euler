from euler import simplify_fraction


def solution() -> int:
    # Sometimes...thinking about it and doing it by hand is best!
    # The "smallest" amount you can take off of 3/7 is 1/1,000,000 = so just need to work out what factor to times 3/7 by
    f = 1000000 // 7
    n = 3 * f - 1
    d = f * 7
    return simplify_fraction(n, d)[0]


if __name__ == "__main__":
    print(solution())
