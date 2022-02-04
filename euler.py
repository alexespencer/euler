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
