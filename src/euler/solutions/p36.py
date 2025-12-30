from euler import is_palindrome


def solution() -> int:
    return sum(
        x for x in range(1, 1_000_000 + 1) if is_palindrome(x) and is_palindrome(x, 2)
    )


if __name__ == "__main__":
    print(solution())
