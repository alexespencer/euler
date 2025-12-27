from euler import fibonacci_seq


def solution() -> int:
    return sum(x for x in fibonacci_seq(4_000_000) if x % 2 == 0)


if __name__ == "__main__":
    print(solution())
