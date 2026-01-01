from math import comb


def solution():
    greater_1m = 0
    for n in range(23, 101):
        for r in range(2, 101):
            if r > n:
                continue

            if comb(n, r) > 1000000:
                greater_1m += 1

    return greater_1m


if __name__ == "__main__":
    print(solution())
