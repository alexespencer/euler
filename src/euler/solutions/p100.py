# One of my proudest Euler moments...the HCF of a/d becomes the HCF of the NEXT item in the sequence between a/b
# And the HCF of c/b becomes the HCF of c/d
# Now we need to determine a/b from this information...
# This series is a form of Pell's number series: https://en.wikipedia.org/wiki/Pell_number
# Which is an approximation of root 2


def find_bag_50pc(limit):
    ab, ad, bc, cd = 3, 5, 7, 2
    iterations = 0
    odd = True
    while True:
        iterations += 1
        b = ab * bc if odd else ad * cd + 1

        # The block below isn't needed, but is a sanity check. Given we get to 10 ** 12 in just 15 iterations leave it in
        a = ab * ad
        c = a - 1
        d = b - 1
        assert b * d == 2 * a * c

        if b > limit:
            break

        # Next in the series
        ab = ad
        cd = bc

        if odd:
            bc = ad + bc
            ad += bc
        else:
            ad += bc
            bc += ad

        odd = not odd

    return b, a, iterations


def solution() -> int:
    limit = 10**12
    total_balls, blue_balls, _ = find_bag_50pc(limit)

    assert total_balls * (total_balls - 1) == 2 * blue_balls * (blue_balls - 1)

    return blue_balls


if __name__ == "__main__":
    print(solution())
