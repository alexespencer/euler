from math import factorial


def solution() -> int:
    factorials = {str(i): factorial(i) for i in range(0, 10)}

    total = 0

    for n in range(10, 999999):
        if n == sum(factorials[digit] for digit in str(n)):
            total += n

    return total


if __name__ == "__main__":
    print(solution())
