import pytest

from euler import pentagon_n, quadratic_equation, is_pentagon_number, reverse_and_add
from euler import is_prime, find_factors, is_composite_number
from euler import prime_factors, is_palindrome

from euler import triangle_n, square_n, hexagonal_n, heptagonal_n, octagonal_n
from euler import is_cube, is_square, continued_expansion, HCF, LCM

class TestEuler:
    def test_pentagon(self):
        # Test pengtagon numbers
        assert list(map(pentagon_n, range(1, 11))) == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        assert all([is_pentagon_number(n) for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]])
        assert all([is_pentagon_number(n + 1) == False for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]])

    @pytest.mark.parametrize("a, b, c, p1, p2",
                                [(1, -3, 2, 2, 1),
                                (1, 5, 6, -2, -3),
                                (3, -6, 3, 1, 1),
                                (-3, -24, -48, -4, -4),
                                (1, 2, 0, 0, -2)])
    def test_quad_no_error(self, a, b, c, p1, p2):
        assert quadratic_equation(a, b, c) == (p1, p2)

    def test_quad_error(self):
        with pytest.raises(ValueError) as e_info:
            quadratic_equation(2, -4, 7)

    @pytest.mark.parametrize("n, prime",
                                [(1, False),
                                (2, True),
                                (3, True),
                                (4, False),
                                (5, True),
                                (9, False),
                                (10, False),
                                (1001621, True)])
    def test_prime(self, n, prime):
        assert is_prime(n) == prime

    def test_sum_prime(self):
        # Sum of primes under 10
        assert 17 == 2 + sum([n for n in range(3, 10, 2) if is_prime(n)])

    @pytest.mark.parametrize("n, factors",
                                [(1, [1]),
                                (2, [1, 2]),
                                (3, [1, 3]),
                                (4, [1, 2, 4]),
                                (5, [1, 5]),
                                (9, [1, 3, 9]),
                                (10, [1, 10, 2, 5])])
    def test_factors(self, n, factors):
        assert list(find_factors(n)) == factors

    def test_composite(self):
        under_100 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]

        for n in range(2, 101):
            if is_composite_number(n):
                assert n in under_100
            else:
                assert n not in under_100

    @pytest.mark.parametrize("n, expected_prime_factors",
                                [(1, {}),
                                 (2, {2: 1}),
                                 (81, {3: 4}),
                                 (92, {2: 2, 23: 1}),
                                 (182, {2: 1, 7: 1, 13: 1}),
                                 (199, {199: 1}),
                                 (256, {2: 8}),
                                 (300, {2: 2, 3: 1, 5: 2})
                                 ])
    def test_prime_factors(self, n, expected_prime_factors):
        assert prime_factors(n) == expected_prime_factors

    @pytest.mark.parametrize("n, expected_result",
                                [(1, True),
                                (121, True),
                                (122, False),
                                (222, True),
                                (223, False),
                                (333, True),
                                (1223221, True)
                                ])
    def test_palindrome(self, n, expected_result):
        assert is_palindrome(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 2),
                                (121, 121+121),
                                (122, 122+221),
                                (222, 222+222),
                                (223, 223+322),
                                (333, 666),
                                (1223221, 1223221 + 1223221),
                                (349, 1292),
                                (1292 , 4213),
                                (4213, 7337)
                                ])
    def test_palindrome(self, n, expected_result):
        assert reverse_and_add(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 1),
                                (2, 3),
                                (3, 6),
                                (4, 10),
                                (5, 15)
                                ])
    def test_triangle(self, n, expected_result):
        assert triangle_n(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 1),
                                (2, 4),
                                (3, 9),
                                (4, 16),
                                (5, 25)
                                ])
    def test_square(self, n, expected_result):
        assert square_n(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 1),
                                (2, 6),
                                (3, 15),
                                (4, 28),
                                (5, 45)
                                ])
    def test_hex(self, n, expected_result):
        assert hexagonal_n(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 1),
                                (2, 7),
                                (3, 18),
                                (4, 34),
                                (5, 55)
                                ])
    def test_hep(self, n, expected_result):
        assert heptagonal_n(n) == expected_result

    @pytest.mark.parametrize("n, expected_result",
                                [(1, 1),
                                (2, 8),
                                (3, 21),
                                (4, 40),
                                (5, 65)
                                ])
    def test_oct(self, n, expected_result):
        assert octagonal_n(n) == expected_result

    def test_cube(self):
        assert is_cube(41063625) == True
        assert is_cube(41063626) == False
        assert is_cube(8) == True

    def test_is_square(self):
        assert is_square(4) == True
        assert is_square(5) == False
        assert is_square(9) == True

    @pytest.mark.parametrize("period, vals",
    [
        (1, [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]),
        (2, [3, 6, 8, 11, 12, 15, 18, 20, 24, 27]),
        (3, [41, 130, 269, 370, 458]),
        (4, [7, 14, 23, 28, 32, 33, 34, 47, 55, 60]),
        (5, [13, 29, 53, 74, 85, 89, 125, 173, 185, 218]),
        (6, [19, 21, 22, 45, 52, 54, 57, 59, 70, 77]),
        (7, [58, 73, 202, 250, 274, 314, 349, 425]),
        (8, [31, 44, 69, 71, 91, 92, 108, 135, 153, 158]),
        (9, [106, 113, 137, 149, 265, 389, 493]),
        (10, [43, 67, 86, 93, 115, 116, 118, 129, 154])]
                )
    def test_continued_expansion(self, period, vals):
        for n in vals:
            assert len(continued_expansion(n)) - 1 == period

    @pytest.mark.parametrize("a, b, hcf", [
                                (8, 4, 4),
                                (4, 8, 4),
                                (12, 16, 4),
                                (9, 12, 3),
                                (7, 8, 1)
                                ])
    def test_HCF(self, a, b, hcf):
        assert HCF(a, b) == hcf

    @pytest.mark.parametrize("a, b, lcm", [
                                (4, 6, 12),
                                (4, 10, 20),
                                (2, 6, 6)
                                ])
    def test_LCM(self, a, b, lcm):
        assert LCM(a, b) == lcm