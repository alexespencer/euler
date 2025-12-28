from euler import fibonacci_seq


def solution() -> int:
    for i, x in enumerate(fibonacci_seq(None)):
        if len(str(x)) >= 1000:
            return i + 1

    raise ValueError("Should not reach here")


if __name__ == "__main__":
    print(solution())
