from math import inf


def solution() -> int:
    max_k = 12000
    limit = 2 * max_k  # any minimal product-sum n for k will satisfy n <= 2k

    # minimal[n] will hold minimal product-sum for k == index
    minimal = [inf] * (max_k + 1)

    # recursive generator of factor combinations (non-decreasing factors)
    # prod: current product; factor_sum: current sum of factors; count: number of factors used;
    # start: smallest factor allowed next (enforces non-decreasing order)
    def search(start: int, prod: int, factor_sum: int, count: int) -> None:
        # try next factor f >= start
        for f in range(start, (limit // prod) + 1):
            new_prod = prod * f
            if new_prod > limit:
                break
            new_sum = factor_sum + f
            new_count = count + 1

            # compute k = product - sum + count (number of terms including 1s)
            k = new_prod - new_sum + new_count
            if k <= max_k:
                # if we've found a smaller n for this k, record it
                if new_prod < minimal[k]:
                    minimal[k] = new_prod

            # prune: if new_prod is already >= minimal[k] (for this k) then deeper factors
            # will only increase product further, so skip deeper recursion for this path.
            # Also if new_prod > limit we break above already.
            if new_prod < limit:
                search(f, new_prod, new_sum, new_count)

    # start recursion with product=1, sum=0, count=0, allowing factors >= 2
    search(2, 1, 0, 0)

    # sum unique minimal product-sum numbers for k=2..max_k
    result = sum(set(minimal[2:]))
    return int(result)


if __name__ == "__main__":
    print(solution())
