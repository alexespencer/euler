from euler import is_pentagon_number, pentagon_n


def solution() -> int:
    # See if we can find ANY pair
    for j in range(1, 3000):
        n1_p = pentagon_n(j)

        for k in range(j + 1, 3000):
            n2_p = pentagon_n(k)

            if is_pentagon_number(n1_p + n2_p) and is_pentagon_number(n2_p - n1_p):
                return n2_p - n1_p

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solution())
