# Square root convergents

from lib2to3.refactor import get_all_fix_names


def get_fraction_parts(n):
    """
    Returns the numerator and demoninator of a fraction for the nth expansion
    """
    a, b = 1, 2

    # Counter for the number of times the numerator has more digits than the demoninator
    count = 0

    for _ in range(n-1):
        a, b = b, (2 * b + a) # Funky little swap - thanks python
        if len(str(a+b)) > len(str(b)): # Don't forget to add the demoninator to the numerator for the "+1" part
            count += 1
    
    return a, b, count

assert get_fraction_parts(1) == (1, 2, 0)
assert get_fraction_parts(2) == (2, 5, 0)
assert get_fraction_parts(3) == (5, 12, 0)
assert get_fraction_parts(4) == (41-29, 29, 0)
assert get_fraction_parts(5) == (99-70, 70, 0)
assert get_fraction_parts(6) == (239-169, 169, 0)
assert get_fraction_parts(7) == (577-408, 408, 0)
assert get_fraction_parts(8) == (1393-985, 985, 1)

a, b, count = get_fraction_parts(1000)
print(count)