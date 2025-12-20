from euler import is_square

# https://en.wikipedia.org/wiki/Periodic_continued_fraction


def continued_fraction(S):
    m = 0
    d = 1
    a0 = int(S**0.5)
    a = a0
    exapansion = [a]

    # The algorithm terminates when this triplet is the same as one encountered before. The algorithm can also terminate on ai when ai = 2 a0
    while True:
        m = d * a - m
        d = (S - m * m) / d

        a = int((a0 + m) / d)
        exapansion.append(a)
        if a == 2 * a0:
            break

    return exapansion


def solution() -> int:
    num_odd = 0
    for n in range(2, 10000 + 1):
        if not is_square(n):
            period = len(continued_fraction(n)) - 1
            if period % 2 == 1:
                num_odd += 1

    return num_odd


if __name__ == "__main__":
    print(solution())
