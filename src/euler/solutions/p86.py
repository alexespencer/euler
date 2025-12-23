# Optimized solution for Problem 86 using Pythagorean triples
# Replaces brute-force triple loop by enumerating Pythagorean triples
# and counting the valid (w,h) splits for each (a = w+h, l) pair.
#
# This implementation uses the project's existing fast_pythag_triples
# generator to enumerate primitive triples and then scales them.

from math import sqrt

from euler import fast_pythag_triples


def solution() -> int:
    TARGET = 1_000_000

    # A safe upper bound for the search
    max_M = 20_000

    # counts_by_length[l] = number of valid cuboids whose longest side == l
    counts_by_length = [0] * (max_M + 1)

    # w + h can be at most 2*M
    limit_a = 2 * max_M

    # We need to know how far to generate primitive triples by hypotenuse.
    # Hypotenuse c for a triangle with legs (a <= 2M, l <= M) satisfies:
    # c^2 = a^2 + l^2 <= (2M)^2 + M^2 = 5 M^2
    # So c <= sqrt(5) * M. Use a small margin.
    max_c = int(sqrt(5.0) * max_M) + 2

    # Enumerate primitive triples with hypotenuse < max_c using provided generator.
    # fast_pythag_triples yields primitive triples (a0, b0, c0).
    for a0, b0, c0 in fast_pythag_triples(max_c):
        # consider both leg orderings: (a = w+h, l = length) can map to either leg
        for leg_a0, leg_l0 in ((a0, b0), (b0, a0)):
            k = 1
            # scale the primitive triple
            while True:
                a = leg_a0 * k
                L = leg_l0 * k

                # If both exceed the relevant limits, further scaling won't help.
                if a > limit_a and L > max_M:
                    break

                if a <= limit_a and 1 <= L <= max_M:
                    # For given a = w + h and l, the valid w values satisfy:
                    # ceil(a/2) <= w <= min(l, a-1)
                    lo = (a + 1) // 2
                    hi = min(L, a - 1)
                    if hi >= lo:
                        counts_by_length[L] += hi - lo + 1

                k += 1

    # Accumulate counts by maximum side and find smallest M reaching TARGET
    total = 0
    for M in range(1, max_M + 1):
        total += counts_by_length[M]
        if total >= TARGET:
            return M

    # If not found within max_M, instruct to raise bound
    raise ValueError("Increase max_M limit")


if __name__ == "__main__":
    print(solution())
