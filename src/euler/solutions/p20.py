from math import factorial


def solution() -> int:
    return sum(map(int, str(factorial(100))))


if __name__ == "__main__":
    print(solution())
