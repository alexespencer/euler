def solution() -> int:
    numbers = set()
    for a in range(2, 100 + 1):
        for b in range(2, 100 + 1):
            numbers.add(a**b)
    return len(numbers)


if __name__ == "__main__":
    print(solution())
