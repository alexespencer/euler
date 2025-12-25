# Find the last ten digits of this prime number: 28433 * (2 ** 7830457) + 1
# Can we just keep the last 10 digits (throwing away the rest) and multiply by 2 each time, up to the required n?


def p97(mult: int, base: int, power: int, digits: int = 10) -> int:
    x = mult

    for _ in range(power):
        x = x * base

        # Now limit x to the last 10 digits
        x = x % (10**digits)

    return x


def solution() -> int:
    assert p97(2354, 2, 60) == int((str(2354 * (2**60)))[-10:])

    answer = p97(28433, 2, 7830457) + 1
    return int(str(answer)[-10:])


if __name__ == "__main__":
    print(solution())
