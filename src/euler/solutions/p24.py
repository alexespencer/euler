from itertools import permutations


def solution() -> int:
    for i, x in enumerate(permutations(range(10), 10)):
        if i == 1_000_000 - 1:
            return int("".join(map(str, x)))

    raise ValueError("Should not reach here")


if __name__ == "__main__":
    print(solution())
