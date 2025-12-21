import itertools
from functools import reduce
from math import prod, sqrt

from euler.primes import is_prime, prime_factors


def pentagon_n(n):
    """Returns the nth pentagon number"""
    return n * (3 * n - 1) // 2


def is_pentagonal(n):
    """
    returns boolean whether n is a solution to (3*m**2 - m)
    (Using quadratic equation)
    """
    if (1 + (1 + 24 * n) ** 0.5) % 6 == 0:
        return True

    return False


def triangle_n(n):
    """Returns the nth triangle number"""
    return n * (n + 1) // 2


def is_triangular(n):
    """
    returns boolean whether n is a triangular number,
    i.e. whether there exits m such that n = m(m+1)/2 >> 0 = -m^2 - m + 2n
    (Using quadratic equation)
    """
    if (-1 + (1 + 8 * n) ** 0.5) % 2 == 0:
        return True

    return False


def square_n(n):
    """Returns the square of a number"""
    return n * n


def hexagonal_n(n):
    """Returns the nth hexagonal number"""
    return n * (2 * n - 1)


def heptagonal_n(n):
    """Returns the nth heptagonal number"""
    return n * (5 * n - 3) // 2


def octagonal_n(n):
    """Returns the nth octagonal number"""
    return n * (3 * n - 2)


def is_cube(n):
    """Returns if a number is a cube"""
    return round(n ** (1 / 3)) ** 3 == n


def is_square(n):
    """Returns if a number is a cube"""
    return round(n ** (1 / 2)) ** 2 == n


def is_pentagon_number(number):
    """Returns true if this number is a pentagon number. Must be given an int"""
    try:
        if (0.5 + sqrt(0.25 + 6 * number)) % 3.0 == 0:
            return True
        else:
            return False
    except Exception:
        return False


def quadratic_equation(a, b, c):
    b2_4ac = (b * b) - (4 * a * c)
    if 2 * a == 0 or b2_4ac < 0:
        raise ValueError("No solution")

    return ((-b + sqrt(b2_4ac)) / (2 * a), (-b - sqrt(b2_4ac)) / (2 * a))


def fibonacci_seq(max_n=None):
    """Returns a list of fibonacci numbers up to max_n"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        if max_n and a > max_n:
            break


def find_factors(n):
    """Returns the factors of n (must be an int)"""
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def count_factors(n):
    pf = prime_factors(n)

    return prod([v + 1 for v in pf.values()])


def is_composite_number(n):
    """Returns if a number is a composite number. A composite number is a whole number with 2 factors (other than 1 and itself) and is not prime"""
    if is_prime(n):
        return False

    if n in [1, 2]:
        return False

    for i in range(2, n):
        if n % i == 0:
            return True

    return False


def list_count_distinct_prime_factor_sieve(N):
    A = [0] * (1 + N)
    for p in range(2, 1 + N):
        if A[p]:
            continue
        for n in range(p, 1 + N, p):
            A[n] += 1
    return A


def list_distinct_prime_factor_sieve(N):
    A = [[] for _ in range(1 + N)]
    for p in range(2, 1 + N):
        if A[p]:
            continue
        for n in range(p, 1 + N, p):
            A[n].append(p)
    return A


def is_palindrome(n):
    """Returns if a number is a palindrome"""
    return str(n) == str(n)[::-1]


def reverse_and_add(n):
    """Returns the sum of the reverse of a number and the number"""
    return n + int(str(n)[::-1])


def continued_expansion(S):
    m = 0
    d = 1
    a0 = int(S**0.5)
    a = a0
    expansion = [a]

    # The algorithm terminates when this triplet is the same as one encountered before. The algorithm can also terminate on ai when ai = 2 a0
    while True:
        m = d * a - m
        d = (S - m * m) / d

        a = int((a0 + m) / d)
        expansion.append(a)
        if a == 2 * a0:
            break

    return expansion


def HCF(a, b):
    """Finds the HCF of two numbers"""
    while b:
        a, b = b, a % b
    return a


def LCM(a, b):
    """Finds the LCM of two numbers"""
    return a * b // HCF(a, b)


def LCM_list(L):
    """Finds the LCM of a list of numbers"""
    return reduce(LCM, L)


def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n + 1):
        phi_set[i] = i

    for i in range(2, n + 1):
        if phi_set[i] == i:
            for j in range(i, n + 1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set


def unique_product_from_factors(
    factors_lookup, number, depth=0, current_products=None, master_list=None
):
    # This functio will be called recursively until number is prime
    # Given a list of a numbers factors, return all the unique ways of multiplying them together (with repetition if needed) to get the original number
    # For example, given the factors [1, 2, 3, 4, 6, 12] and the number 12, return [[1, 12], [2, 6], [3, 4], [1, 2, 6], [1, 3, 4], [1, 2, 3, 4]]
    if master_list is None:
        master_list = []

    if current_products is None:
        my_products = []
    else:
        my_products = current_products.copy()

    # Check if the number is in factors_lookup (a dict, so if we edit it, it will be changed for all future calls)
    if number not in factors_lookup:
        factors_lookup[number] = find_factors(number)

    my_products.append(number)
    # print(f"{'-'*depth} Number: {number}, Current products: {my_products} ({prod(my_products)})")
    master_list.append(my_products.copy())

    # Call this function for each factor of this number (except 1 and itself)
    for factor in factors_lookup[number]:
        if factor == 1 or factor == number:
            continue

        my_products[-1] = number // factor
        # Divide the last element by this factor before calling
        unique_product_from_factors(
            factors_lookup,
            factor,
            depth + 1,
            current_products=my_products,
            master_list=master_list,
        )

    if depth == 0:
        # Sort each of the lists in master_list
        for i, L in enumerate(master_list):
            master_list[i] = sorted(L)

        master_list.sort()
        master_list = list(k for k, _ in itertools.groupby(master_list))

        return master_list


def is_product_sum(current_prod, product_factors, k):
    # Get the pad count
    pad_count = k - len(product_factors)

    return current_prod == sum(product_factors) + pad_count


def _pythag_triples(m, n, max_length):
    triples = []

    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    k = 1
    while True:
        if (k * a) + (k * b) + (k * c) > max_length:
            break

        triples.append(tuple(sorted([k * a, k * b, k * c])))
        k += 1

    return triples


def generate_pythag_triples(max_length):
    """Generates all pythaga triples up to max_length"""
    # What is the max value of m we need to use?
    m = 2
    while True:
        if _pythag_triples(m, 1, max_length):
            m += 1
        else:
            break

    # Generate all triangles up to our max length
    max_m = m * 2
    triangles = {}
    for m in range(2, max_m):
        # If m is odd then n cannot also be odd so we get to skip every other n
        step = 1 if m % 2 == 0 else 2
        for n in range(step, m, step):
            if HCF(m, n) == 1:
                for triple in _pythag_triples(m, n, max_length):
                    length = sum(triple)
                    triangles.setdefault(length, []).append(triple)

    # Sometimes we can generate things like (12, 16, 20), (12, 16, 20) - from different m/n pairs - so make them unique now
    for length, triples in triangles.items():
        triangles[length] = set(triples)

    return triangles


def fast_pythag_triples(k):  # k is the max length of the hypotenuse
    """Returns a list of all pythagorean triples with a hypotenuse less than k, (a, b, c) or (b, a, c) - be careful"""
    n, m = 1, 2
    while m * m + 1 < k:
        if n >= m:
            n, m = m % 2, m + 1
        c = m * m + n * n
        if c >= k:
            n = m
            continue
        if HCF(n, m) == 1:
            yield m * m - n * n, 2 * m * n, c
        n += 2


class Calculation:
    def __init__(self, number1, operator=None, number2=None):
        self.number1 = number1
        self.operator = operator
        self.number2 = number2
        self.result = self.calc()
        self.number_set = self.numbers_used()

    def __eq__(self, other):
        # Everything has to be the same
        if not isinstance(other, Calculation):
            return False
        if self.result != other.result:
            return False
        if self.operator != other.operator:
            return False
        if self.number1 != other.number1:
            return False
        if self.number2 != other.number2:
            return False

        return True

    def __hash__(self):
        return hash((self.number1, self.operator, self.number2))

    def numbers_used(self):
        numbers_used = []
        if isinstance(self.number1, int):
            numbers_used.append(self.number1)
        else:
            numbers_used.extend(self.number1.numbers_used())
        if isinstance(self.number2, int):
            numbers_used.append(self.number2)
        elif self.number2 is not None:
            numbers_used.extend(self.number2.numbers_used())

        return set(numbers_used)

    def __repr__(self):
        if self.operator is None:
            return f"{self.number1}"

        return f"({repr(self.number1)} {self.operator} {repr(self.number2)})"

    def __str__(self):
        return str(self.result)

    def __add__(self, other):
        if isinstance(other, int):
            return Calculation(self.result, "+", other)

        return Calculation(self.result, "+", other.result)

    def __sub__(self, other):
        if isinstance(other, int):
            return Calculation(self.result, "-", other)
        return Calculation(self.result, "-", other.result)

    def __mul__(self, other):
        if isinstance(other, int):
            return Calculation(self.result, "*", other)
        return Calculation(self.result, "*", other.result)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Calculation(self.result, "/", other)
        return Calculation(self.result, "/", other.result)

    def calc(self):
        if isinstance(self.number1, Calculation):
            left = self.number1.calc()
        else:
            left = self.number1

        if isinstance(self.number2, Calculation):
            right = self.number2.calc()
        else:
            right = self.number2

        if self.operator == "+":
            return left + right
        elif self.operator == "-":
            return left - right
        elif self.operator == "*":
            return left * right
        elif self.operator == "/":
            return left / right
        elif self.operator is None:
            return left
        else:
            raise ValueError("Unknown operator")


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def is_prime_miller_rabin(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(
        _try_composite(a, d, n, s) for a in _known_primes[:_precision_for_huge_n]
    )


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
