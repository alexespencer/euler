from math import prod


def solution() -> int:
    seek_digits = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
    found_digits = []
    curr_digit_count = 0
    n = 0

    while seek_digits:
        n += 1
        str_n = str(n)
        digit_start = curr_digit_count
        digit_end = curr_digit_count + len(str_n)
        while seek_digits and digit_start <= seek_digits[0] <= digit_end:
            seek_digit = seek_digits.pop(0)
            found_digits.append(int(str_n[seek_digit - digit_start - 1]))
        curr_digit_count = digit_end

    return prod(found_digits)


if __name__ == "__main__":
    print(solution())
