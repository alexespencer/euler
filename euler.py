from math import sqrt

def pentagon_n(n):
    """Returns the nth pentagon number"""
    return int(n * (3 * n - 1) / 2)

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
    factors = []

    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)

    return factors

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
            p += 1

    n = int(n)
    factors.setdefault(n, 0)
    factors[n] += 1

    return factors
