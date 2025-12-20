# Square root convergents
def get_fraction_parts(n):
    """
    Returns the numerator and demoninator of a fraction for the nth expansion
    """
    numerator, denominator = 1, 2

    # Counter for the number of times the numerator has more digits than the demoninator
    count = 0

    for i in range(1, n):
        numerator, denominator = (
            denominator,
            (2 * denominator + numerator),
        )
        if len(str(numerator + denominator)) > len(
            str(denominator)
        ):  # Don't forget to add the demoninator to the numerator for the "+1" part
            count += 1

    return numerator, denominator, count


def solution() -> int:
    assert get_fraction_parts(1) == (1, 2, 0)
    assert get_fraction_parts(2) == (2, 5, 0)
    assert get_fraction_parts(3) == (5, 12, 0)
    assert get_fraction_parts(4) == (41 - 29, 29, 0)
    assert get_fraction_parts(5) == (99 - 70, 70, 0)
    assert get_fraction_parts(6) == (239 - 169, 169, 0)
    assert get_fraction_parts(7) == (577 - 408, 408, 0)
    assert get_fraction_parts(8) == (1393 - 985, 985, 1)

    _, _, count = get_fraction_parts(1000)
    return count


if __name__ == "__main__":
    print(solution())
