from euler import find_factors


def solution() -> int:
    # Find abundant numbers up to 28123
    abundant = set()
    for i in range(1, 28123 + 1):
        factors = find_factors(i)
        if sum(factors) - i > i:
            abundant.add(i)

    # Create set of integers that can be written as the sum of 2 abundant numbers
    two_abundant_sums = set()
    for a in abundant:
        for b in abundant:
            two_abundant_sums.add(a + b)

    # Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
    return sum([i for i in range(1, 28123 + 1) if i not in two_abundant_sums])


if __name__ == "__main__":
    print(solution())
