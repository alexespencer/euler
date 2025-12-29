def n_is_sum_of_y_powers_of_digits(n: int, y: int):
    return n == sum(int(x) ** y for x in str(n))


def solution() -> int:
    assert n_is_sum_of_y_powers_of_digits(1634, 4) is True

    return sum(
        n for n in range(2, 5 * 9**5 + 1) if n_is_sum_of_y_powers_of_digits(n, 5)
    )


if __name__ == "__main__":
    print(solution())
