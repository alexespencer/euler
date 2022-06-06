# In python this is made easier by the decimal library where you can set the precision of a float to 100 places
# If that didn't exist, we could probably do some clever recursion in combination with our infinite fraction code from earlier problems combined with long division

import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import is_square

from decimal import Decimal, getcontext
getcontext().prec = 110

def digit_sum_sqrt(n):
    # Square root the number
    d = Decimal(n).sqrt()

    # Convert to string
    strd = str(d)

    # Keep 100 digits after the first decimal point
    strd = strd[:strd.index('.') + 100]

    # assert len(strd) == 100
    return sum(int(x) for x in strd if x != '.')

print(digit_sum_sqrt(2))
print("Running tests...")
assert digit_sum_sqrt(2) == 475
print("----")

# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
print(sum(digit_sum_sqrt(n) for n in range(1, 100+1) if not is_square(n)))

# Note: it wasn't immediately clear that they also wanted the "int" part of the sum ie in root(2) 1.4.... - they want the "1" included in the "decimal digits" - but it ISN'T a "decimal" digit, is it?