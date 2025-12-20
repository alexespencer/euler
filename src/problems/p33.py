import math
from datetime import datetime
from fractions import Fraction
from posixpath import curdir

start_time = datetime.now()

N = 2
K = 1


def count_cancellable_digits(number1, number2):
    str_1 = str(number1)
    str_2 = str(number2)
    digits_in_common = set(str_1).intersection(set(str_2))
    return sum(
        [min(str_1.count(digit), str_2.count(digit)) for digit in digits_in_common]
    )


def generate_cancellable_fractions(N, K):
    set_n = [
        (str(n), set(str(n)), {str(d): str(n).count(str(d)) for d in range(10)})
        for n in range(10**N)
    ]

    cancellable_fractions = []
    for n in range(10 ** (N - 1), 10**N):
        print(f"{n=}")
        for d in range(n + 1, 10**N):
            print(f"{d=}")
            digits_in_common = set_n[n][1].intersection(set_n[d][1])
            if (
                sum(
                    [
                        min(set_n[n][2][digit], set_n[d][2][digit])
                        for digit in digits_in_common
                    ]
                )
                >= K
            ):
                cancellable_fractions.append((n, d))

    return cancellable_fractions


assert count_cancellable_digits(1234, 123) == 3
assert count_cancellable_digits(1234, 567) == 0
assert count_cancellable_digits(1234, 1234) == 4
assert count_cancellable_digits(1234, 4321) == 4
assert count_cancellable_digits(1234, 4322) == 3


# Generate numbers without trailing zeros
def fractions():
    numbers = {
        x: "".join(sorted(set(str(x))))
        for x in range(10 ** (N - 1), 10**N)
        if x % 10 != 0
    }

    fractions = [
        (n, d)
        for n in numbers
        for d in numbers
        if n < d and count_cancellable_digits(n, d) >= K
    ]
    return fractions


def curious_fraction(n, d, k, orig_fraction=None):
    # Can we delete k digits from n/d and end up with the same fraction
    orig = Fraction(n, d)
    if orig_fraction is None:
        orig_fraction = orig
    n_digit_set = set(str(n))
    d_digit_set = set(str(d))

    # Pick a digit from the intersection
    for digit in n_digit_set.intersection(d_digit_set):
        # Get indexes of this digit
        n_digit_indexes = [i for i, x in enumerate(str(n)) if x == digit]
        d_digit_indexes = [i for i, x in enumerate(str(d)) if x == digit]

        # Cartesian test
        for index1 in n_digit_indexes:
            n_new = int(str(n)[:index1] + str(n)[index1 + 1 :])
            for index2 in d_digit_indexes:
                # Remove this index
                d_new = int(str(d)[:index2] + str(d)[index2 + 1 :])

                if k == 1:
                    new_fraction = Fraction(n_new, d_new)
                    if new_fraction == orig_fraction:
                        return True
                else:
                    next_level = curious_fraction(
                        n_new, d_new, k - 1, orig_fraction=orig
                    )
                    if next_level:
                        return True

    # Tried all digits, no match
    return False


def simplify_fraction(n: int, d: int) -> tuple[int, int]:
    gcd = math.gcd(n, d)
    return (n // gcd, d // gcd)


def solution() -> int:
    # TODO: move these asserts into tests
    assert curious_fraction(49, 98, 1)
    assert not curious_fraction(449, 494, 2)
    assert curious_fraction(3016, 6032, 3)

    prod_n, prod_d = 1, 1
    curious_fractions = []
    for n, d in fractions():
        if curious_fraction(n, d, K):
            curious_fractions.append((n, d))
            prod_n *= n
            prod_d *= d
    return simplify_fraction(prod_n, prod_d)[1]  # Return denominator


if __name__ == "__main__":
    print(solution())
