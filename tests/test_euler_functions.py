from math import prod

import pytest

from euler import (
    HCF,
    LCM,
    Calculation,
    continued_expansion,
    count_factors,
    decimal_digits,
    decimal_repeat_cycle_length,
    fibonacci_seq,
    find_factors,
    generate_pythag_triples,
    heptagon_n,
    hexagon_n,
    is_composite_number,
    is_cube,
    is_palindrome,
    is_pentagon_number,
    is_pentagonal,
    is_prime,
    is_prime_miller_rabin,
    is_product_sum,
    is_square,
    is_triangular,
    list_count_distinct_prime_factor_sieve,
    list_distinct_prime_factor_sieve,
    octagon_n,
    pentagon_n,
    phi_1_to_n,
    prime_factors,
    quadratic_equation,
    reverse_and_add,
    simplify_fraction,
    square_n,
    triangle_n,
    unique_product_from_factors,
)


def test_fibonacci():
    assert list(fibonacci_seq(55)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_factor_sieve():
    A = list_distinct_prime_factor_sieve(20)
    assert A == [
        [],
        [],
        [2],
        [3],
        [2],
        [5],
        [2, 3],
        [7],
        [2],
        [3],
        [2, 5],
        [11],
        [2, 3],
        [13],
        [2, 7],
        [3, 5],
        [2],
        [17],
        [2, 3],
        [19],
        [2, 5],
    ]
    assert list_count_distinct_prime_factor_sieve(20) == [
        0,
        0,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        2,
        1,
        1,
        2,
        1,
        2,
    ]


def test_pentagon():
    # Test pengtagon numbers
    assert list(map(pentagon_n, range(1, 11))) == [
        1,
        5,
        12,
        22,
        35,
        51,
        70,
        92,
        117,
        145,
    ]
    assert all(
        [is_pentagon_number(n) for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]]
    )
    assert all(
        [
            not is_pentagon_number(n + 1)
            for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        ]
    )

    assert all([is_pentagonal(n) for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]])
    assert all(
        [not is_pentagonal(n + 1) for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]]
    )


@pytest.mark.parametrize(
    "a, b, c, p1, p2",
    [
        (1, -3, 2, 2, 1),
        (1, 5, 6, -2, -3),
        (3, -6, 3, 1, 1),
        (-3, -24, -48, -4, -4),
        (1, 2, 0, 0, -2),
    ],
)
def test_quad_no_error(a, b, c, p1, p2):
    assert quadratic_equation(a, b, c) == (p1, p2)


def test_quad_error():
    with pytest.raises(ValueError):
        quadratic_equation(2, -4, 7)


@pytest.mark.parametrize(
    "n, prime",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (9, False),
        (10, False),
        (1001621, True),
    ],
)
def test_prime(n, prime):
    assert is_prime(n) == prime


def test_count_factors():
    for i in range(1, 10**5):
        assert len(find_factors(i)) == count_factors(i)


def test_miller_rabin():
    for i in range(3, 10**6, 2):
        assert is_prime(i) == is_prime_miller_rabin(i)


def test_sum_prime():
    # Sum of primes under 10
    assert 17 == 2 + sum([n for n in range(3, 10, 2) if is_prime(n)])


@pytest.mark.parametrize(
    "n, factors",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 3]),
        (4, [1, 2, 4]),
        (5, [1, 5]),
        (9, [1, 3, 9]),
        (10, [1, 10, 2, 5]),
    ],
)
def test_factors(n, factors):
    assert list(find_factors(n)) == factors


def test_composite():
    under_100 = [
        4,
        6,
        8,
        9,
        10,
        12,
        14,
        15,
        16,
        18,
        20,
        21,
        22,
        24,
        25,
        26,
        27,
        28,
        30,
        32,
        33,
        34,
        35,
        36,
        38,
        39,
        40,
        42,
        44,
        45,
        46,
        48,
        49,
        50,
        51,
        52,
        54,
        55,
        56,
        57,
        58,
        60,
        62,
        63,
        64,
        65,
        66,
        68,
        69,
        70,
        72,
        74,
        75,
        76,
        77,
        78,
        80,
        81,
        82,
        84,
        85,
        86,
        87,
        88,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        98,
        99,
        100,
    ]

    for n in range(2, 101):
        if is_composite_number(n):
            assert n in under_100
        else:
            assert n not in under_100


@pytest.mark.parametrize(
    "n, expected_prime_factors",
    [
        (1, {}),
        (2, {2: 1}),
        (81, {3: 4}),
        (92, {2: 2, 23: 1}),
        (182, {2: 1, 7: 1, 13: 1}),
        (199, {199: 1}),
        (256, {2: 8}),
        (300, {2: 2, 3: 1, 5: 2}),
        (25**12, {5: 24}),
    ],
)
def test_prime_factors(n, expected_prime_factors):
    assert prime_factors(n) == expected_prime_factors


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (1, True),
        (121, True),
        (122, False),
        (222, True),
        (223, False),
        (333, True),
        (1223221, True),
    ],
)
def test_palindrome(n, expected_result):
    assert is_palindrome(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result",
    [
        (1, 2),
        (121, 121 + 121),
        (122, 122 + 221),
        (222, 222 + 222),
        (223, 223 + 322),
        (333, 666),
        (1223221, 1223221 + 1223221),
        (349, 1292),
        (1292, 4213),
        (4213, 7337),
    ],
)
def test_reverse_and_add(n, expected_result):
    assert reverse_and_add(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result", [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15)]
)
def test_triangle(n, expected_result):
    assert triangle_n(n) == expected_result
    assert is_triangular(expected_result)


@pytest.mark.parametrize(
    "n, expected_result", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
)
def test_square(n, expected_result):
    assert square_n(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result", [(1, 1), (2, 6), (3, 15), (4, 28), (5, 45)]
)
def test_hex(n, expected_result):
    assert hexagon_n(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result", [(1, 1), (2, 7), (3, 18), (4, 34), (5, 55)]
)
def test_hep(n, expected_result):
    assert heptagon_n(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result", [(1, 1), (2, 8), (3, 21), (4, 40), (5, 65)]
)
def test_oct(n, expected_result):
    assert octagon_n(n) == expected_result


def test_cube():
    assert is_cube(41063625)
    assert not is_cube(41063626)
    assert is_cube(8)


def test_is_square():
    assert is_square(4)
    assert not is_square(5)
    assert is_square(9)


@pytest.mark.parametrize(
    "period, vals",
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
        (10, [43, 67, 86, 93, 115, 116, 118, 129, 154]),
    ],
)
def test_continued_expansion(period, vals):
    for n in vals:
        assert len(continued_expansion(n)) - 1 == period


@pytest.mark.parametrize(
    "a, b, hcf", [(8, 4, 4), (4, 8, 4), (12, 16, 4), (9, 12, 3), (7, 8, 1)]
)
def test_HCF(a, b, hcf):
    assert HCF(a, b) == hcf


@pytest.mark.parametrize("a, b, lcm", [(4, 6, 12), (4, 10, 20), (2, 6, 6)])
def test_LCM(a, b, lcm):
    assert LCM(a, b) == lcm


@pytest.mark.parametrize(
    "n, expected_set",
    [
        (4, [1, 1, 2, 2]),
        (10, [1, 1, 2, 2, 4, 2, 6, 4, 6, 4]),
    ],
)
def test_phi(n, expected_set):
    assert phi_1_to_n(n) == {i + 1: v for i, v in enumerate(expected_set)}


@pytest.mark.parametrize(
    "n, expected_set",
    [
        (12, [[2, 2, 3], [2, 6], [3, 4], [12]]),
        (8, [[2, 2, 2], [2, 4], [8]]),
    ],
)
def test_unique_product_from_factors(n, expected_set):
    # Create a factors list that gets reused for optimised lookups
    factors_lookup = {}

    # Call the function
    unique_factors = unique_product_from_factors(factors_lookup, n)

    assert unique_factors == expected_set
    assert unique_factors is not None
    # For each set, check that the product is n
    for s in unique_factors:
        assert prod(s) == n


@pytest.mark.parametrize(
    "n, product_factors, k, expected_result",
    [
        (8, [2, 2, 2], 8, False),
        (8, [2, 2, 2], 5, True),
        (12, [2, 6], 6, True),
    ],
)
def test_is_product_sum(n, product_factors, k, expected_result):
    assert is_product_sum(n, product_factors, k) == expected_result


def test_calculation():
    a = Calculation(1)
    assert str(a) == "1"
    assert repr(a) == "1"
    b = Calculation(5, "*", 3)
    assert str(b) == "15"
    assert repr(b) == "(5 * 3)"
    c = Calculation(a, "+", b)
    assert str(c) == "16"
    assert repr(c) == "(1 + (5 * 3))"
    assert c.numbers_used() == {1, 5, 3}

    d = Calculation(c, "/", 8)
    assert str(d) == "2.0"
    assert repr(d) == "((1 + (5 * 3)) / 8)"
    assert d.numbers_used() == {1, 5, 3, 8}

    e = Calculation(8, "/", c)
    assert str(e) == "0.5"
    assert repr(e) == "(8 / (1 + (5 * 3)))"
    assert e.numbers_used() == {1, 5, 3, 8}


def test_pythag_triples():
    triangles = generate_pythag_triples(234)

    # Run tests (from wiki, all of these are expected to be found)
    pt_100 = [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
        (20, 21, 29),
        (12, 35, 37),
        (9, 40, 41),
        (28, 45, 53),
        (11, 60, 61),
        (16, 63, 65),
        (33, 56, 65),
        (48, 55, 73),
        (13, 84, 85),
        (36, 77, 85),
        (39, 80, 89),
        (65, 72, 97),
    ]

    for triple in pt_100:
        assert triple in triangles[sum(triple)]


def test_simplify_fraction():
    assert simplify_fraction(10, 20) == (1, 2)
    assert simplify_fraction(4, 8) == (1, 2)
    assert simplify_fraction(3, 7) == (3, 7)
    assert simplify_fraction(3 * 15 * 10 * 3 * 19, 7 * 15 * 10 * 3 * 19) == (3, 7)


def test_decimal_digits():
    digits = decimal_digits(1, 2)
    assert next(digits) == (5, 0)
    assert next(digits) == (0, 0)

    digits = decimal_digits(1, 4)
    assert next(digits) == (2, 2)
    assert next(digits) == (5, 0)

    digits = decimal_digits(1, 3)
    assert next(digits) == (3, 1)
    assert next(digits) == (3, 1)

    digits = decimal_digits(1, 7)
    assert next(digits) == (1, 3)
    assert next(digits) == (4, 2)
    assert next(digits) == (2, 6)
    assert next(digits) == (8, 4)
    assert next(digits) == (5, 5)
    assert next(digits) == (7, 1)
    assert next(digits) == (1, 3)  # Repeats now


def test_cycle_length():
    assert decimal_repeat_cycle_length(1, 2) == 0
    assert decimal_repeat_cycle_length(1, 4) == 0
    assert decimal_repeat_cycle_length(1, 6) == 1
    assert decimal_repeat_cycle_length(1, 7) == 6
    assert decimal_repeat_cycle_length(1, 9) == 1
