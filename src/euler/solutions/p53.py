from math import factorial


# TODO: is this a native functon available in math?
# TODO: move out of this module, likely useful elsewhere
def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solution():
    assert combinations(5, 3) == 10
    assert combinations(23, 10) == 1144066

    greater_1m = 0
    for n in range(23, 101):
        for r in range(2, 101):
            if r > n:
                continue

            if combinations(n, r) > 1000000:
                greater_1m += 1

    return greater_1m


if __name__ == "__main__":
    print(solution())
