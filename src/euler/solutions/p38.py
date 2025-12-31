def is_pandigital(n: int) -> bool:
    str_n = str(n)
    if len(str_n) < 9 or "0" in str_n or len(str_n) > 9:
        return False

    return set(str_n) == set("123456789")


def concatenated_product(n: int, N: int):
    """Returns the concatenated product of n and (1, 2, ..., N) where N > 1"""
    assert N > 1
    str_n = ""
    for i in range(1, N + 1):
        str_n += str(n * i)

    return int(str_n)


def solution() -> int:
    assert concatenated_product(192, 3) == 192384576
    assert concatenated_product(9, 5) == 918273645

    max_concat_product = 0

    n = 9
    while True:
        for N in range(2, 10):
            concat_prod = concatenated_product(n, N)

            if N == 2 and concat_prod > 999_999_999:
                return max_concat_product

            if is_pandigital(concat_prod) and concat_prod > max_concat_product:
                max_concat_product = concat_prod
        n += 1


if __name__ == "__main__":
    print(solution())
