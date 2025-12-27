def solution() -> int:
    return (sum(range(1, 100 + 1)) ** 2) - (sum(x**2 for x in range(1, 100 + 1)))


if __name__ == "__main__":
    print(solution())
