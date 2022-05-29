import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import HCF, LCM, find_factors, phi_1_to_n
from functools import reduce

# This one looks familiar...and seems to need us to discover (or determine) the number of possible fractions. Let's see if there is a pattern

def reduce_fraction(numerator, denominator):
    # Reduce the fraction to lowest terms
    while True:
        cd = HCF(numerator, denominator)
        if cd == 1:
            break

        numerator = numerator // cd
        denominator = denominator // cd
    return numerator, denominator

assert reduce_fraction(10, 20) == (1, 2)
assert reduce_fraction(4, 8) == (1, 2)
assert reduce_fraction(3, 7) == (3, 7)
assert reduce_fraction(3*15*10*3*19, 7*15*10*3*19) == (3, 7)

def count_possible_fractions(max_d):
    # We can just sum phi(d) for 2 to max_d
    phi_set = phi_1_to_n(max_d)
    return sum(phi_set.values()) - 1

# Only 98million, we could brute force it?
# Generate fractions up to the max_fraction...this is SLOW, but bearable
starttime = time.time()
possible_fractions = []
for d in range(1, 12000+1):
    if d % 1000 == 0:
        print(d)
    for n in range((d // 3) - 1, (d // 2) + 1):
        if (1/3) < n / d < (1/2):
            rf = reduce_fraction(n, d)
            
            possible_fractions.append(rf)

print(len(set(possible_fractions)))
endtime = time.time()
print(f"Time taken: {endtime - starttime}")