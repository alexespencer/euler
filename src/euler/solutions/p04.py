from euler import is_palindrome


def solution() -> int:
    # Generate 3 digit numbers
    max_found = 0
    three_digit = [x for x in range(100, 1000)]
    for a in three_digit:
        for b in three_digit:
            value = a * b
            if is_palindrome(value):
                max_found = max(max_found, value)

    return max_found


if __name__ == "__main__":
    print(solution())
