# We can just keep track of the last 10 digits (throwing away the rest) - similar to p97


def self_power(base: int, power: int, digits: int = 10) -> int:
    x = 1

    for _ in range(power):
        x = x * base

        # Now limit x to the last x digits
        x = x % (10**digits)

    return x


def solution() -> int:
    assert self_power(1, 1, 10) == 1
    assert self_power(2, 2, 10) == 4
    assert self_power(3, 3, 10) == 27
    assert self_power(4, 4, 10) == 256
    assert self_power(10, 10, 10) == 0

    digits = 0
    for i in range(1, 1000 + 1):
        digits += self_power(i, i, 10)

    return int(str(digits)[-10:])


if __name__ == "__main__":
    print(solution())
