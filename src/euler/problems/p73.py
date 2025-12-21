from euler import simplify_fraction


# Only 98million, we could brute force it?
# Generate fractions up to the max_fraction...this is SLOW, but bearable
def solution() -> int:
    possible_fractions = []
    for d in range(1, 12000 + 1):
        for n in range((d // 3) - 1, (d // 2) + 1):
            if (1 / 3) < n / d < (1 / 2):
                rf = simplify_fraction(n, d)

                possible_fractions.append(rf)

    return len(set(possible_fractions))


if __name__ == "__main__":
    print(solution())
