# In python this is made easier by the decimal library where you can set the precision of a float to 100 places
# If that didn't exist, we could probably do some clever recursion in combination with our infinite fraction code from earlier problems combined with long division


from decimal import Context, Decimal, localcontext

from euler import is_square


def digit_sum_sqrt(n):
    with localcontext(Context(prec=110)):
        # Square root the number
        d = Decimal(n).sqrt()

        # Convert to string
        strd = str(d)

        # Keep 100 digits after the first decimal point
        strd = strd[: strd.index(".") + 100]

        # assert len(strd) == 100
        return sum(int(x) for x in strd if x != ".")


def solution() -> int:
    assert digit_sum_sqrt(2) == 475

    # For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
    return sum(digit_sum_sqrt(n) for n in range(1, 100 + 1) if not is_square(n))


if __name__ == "__main__":
    print(solution())
