from euler import find_factors


class Solution:
    def __init__(self, N=9):
        # Generate factors
        assert 1 <= N <= 9, "N must be between 1 and 9"
        self.pandigits = set([str(i) for i in range(1, N + 1)])
        self.factor_lookup = {
            i: find_factors(i)
            for i in range(1, 10**5)
            if len(str(i)) == len(set(str(i)))
        }

    def solve(self, N):
        assert 1 <= N <= 9, "N must be between 1 and 9"
        self.pandigits = set([str(i) for i in range(1, N + 1)])

        # Find pandigital products
        total_sum = 0
        for f, factors in self.factor_lookup.items():
            found = False
            for factor in factors:
                if found:
                    break

                if self.pandigital_product(f // factor, factor, f):
                    total_sum += f

                    found = True
        return total_sum

    def pandigital_product(self, a, b, prod):
        combined = str(a) + str(b) + str(prod)
        if len(combined) == len(set(combined)) and set(combined) == self.pandigits:
            # print(prod)
            # print(combined)
            # print(len(combined), len(set(combined)), set(combined))
            return True

        return False


s = Solution(9)
assert s.pandigital_product(39, 186, 39 * 186)
assert not s.pandigital_product(39, 183, 39 * 183)

# Sum of all pandigital products for N 9
assert s.solve(9) == 45228

s = Solution()
for N in range(4, 10):
    print(f"Sum of all pandigital products for N {N}: {s.solve(N)}")
