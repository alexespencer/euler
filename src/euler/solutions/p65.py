# start with numerator as 2
# Calculating the 3rd numerator


def solution() -> int:
    desired_nth_convergent_numerator = 100

    numerator = 2
    previous_numerator = 1
    for i in range(2, desired_nth_convergent_numerator + 1):
        multiplier = 2 * int(i / 3) if i % 3 == 0 else 1
        previous_numerator, numerator = (
            numerator,
            previous_numerator + (numerator * multiplier),
        )

    return sum(map(int, str(numerator)))


if __name__ == "__main__":
    print(solution())
