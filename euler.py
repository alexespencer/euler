from math import sqrt
from functools import reduce

def pentagon_n(n):
    """Returns the nth pentagon number"""
    return int(n * (3 * n - 1) / 2)

def triangle_n(n):
    """Returns the nth triangle number"""
    return int(n * (n + 1) / 2)

def square_n(n):
    """Returns the square of a number"""
    return int(n * n)

def hexagonal_n(n):
    """Returns the nth hexagonal number"""
    return int(n * (2 * n - 1))

def heptagonal_n(n):
    """Returns the nth heptagonal number"""
    return int(n * (5 * n - 3) / 2)

def octagonal_n(n):
    """Returns the nth octagonal number"""
    return int(n * (3 * n - 2))

def is_cube(n):
    """Returns if a number is a cube"""
    return round(n ** (1/3)) ** 3 == n

def is_square(n):
    """Returns if a number is a cube"""
    return round(n ** (1/2)) ** 2 == n

def is_pentagon_number(number):
    """Returns true if this number is a pentagon number. Must be given an int"""
    try:
        if (0.5 + sqrt(0.25 + 6 * number)) % 3.0 == 0:
            return True
        else:
            return False
    except:
        return False

def quadratic_equation(a, b, c):
    b2_4ac = (b * b) - (4 * a * c)
    if 2 * a == 0 or b2_4ac < 0:
        raise ValueError("No solution")

    return ((-b + sqrt(b2_4ac))/(2 * a), (-b - sqrt(b2_4ac))/(2 * a))

def is_prime(n):
    """Returns if a number is prime"""
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, int(sqrt(n+1)+1)):
    # for i in range(2, n):
        if n % i == 0:
            return False

    return True

def find_factors(n):
    """Returns the factors of n (must be an int)"""
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

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

def prime_factors(n):
    """Returns a dictionary of prime: order. For example 100 (prime factors 2x2x5x5) would return {2: 2, 5:2}"""
    if n == 1:
        return {}

    p = 2
    factors = {}
    while n >= p * p:
        if n % p == 0:
            factors.setdefault(p, 0)
            factors[p] += 1
            n = n / p
        else:
            if p <= 2:
                p += 1
            else:
                p += 2

    n = int(n)
    factors.setdefault(n, 0)
    factors[n] += 1

    return factors

def is_palindrome(n):
    """Returns if a number is a palindrome"""
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    """Returns the sum of the reverse of a number and the number"""
    return n + int(str(n)[::-1])

def continued_expansion(S):
    m = 0
    d = 1
    a0 = int(S ** 0.5)
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

def LCM_list(l):
    """Finds the LCM of a list of numbers"""
    return reduce(LCM, l)

def phi_1_to_n(n):
    phi_set = {}
    for i in range(1, n+1):
        phi_set[i] = i

    for i in range(2, n+1):
        if phi_set[i] == i:
            for j in range(i, n+1, i):
                phi_set[j] -= int(phi_set[j] / i)

    return phi_set