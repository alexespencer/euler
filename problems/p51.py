import sys, os
print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

import itertools

from euler import is_prime

import time

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number
# is the first example having seven primes among the ten generated numbers, yielding the family:
#  56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
#  with the same digit, is part of an eight prime value family.

# Starting from 56003, for each number:
# 1) generate a mask (never the last digit)
# 2) test each mask to see if it is an eight prime value family (can short-circuit here if > 2 NON primes are found)
# 3) return first number (and it's smallest prime, along with all the others)

# First see if we can find the one in the question (7)

def apply_mask(number, mask, digit):
    # Convert the number to string
    str_num = list(str(number))

    # Replace each masked digit
    for char in mask:
        str_num[char] = str(digit)

    return int(''.join(str_num))

assert apply_mask("56123", (2, 3), 6) == 56663

def p51(number, mask, family_count):
    """Short circuiting function to test if a number and mask has the required number of primes with the logic applied"""
    primes = []
    not_prime_count = 0
    for x in range(0, 10):
        # Apply the mask for each digit 0-9
        num = apply_mask(number, mask, x)

        if x == 0 and 0 in mask:
            # Ensure the number of digits is still the same
            not_prime_count += 1
        elif is_prime(num):
            # If prime found, add it to the list
            primes.append(num)
        else:
            # Otherwise increase our 'not prime' count and if this ever breaches the minimum we can stop the expensive checking of primes
            not_prime_count += 1

        if not_prime_count > 10 - family_count:
            return False, []

    return True, primes

print(p51(56003, (2, 3), 7))
print(p51(13, (0,), 6))
print(p51(13, (0,), 7))

# We can generate masks in advance
def generate_masks(num_digits):
    """Generates a mask array, of digits that will be replaced (0 bound). At least 2 masked but does not include the last digit as unlikely to get > 5 primes
    For example generate_masks(4) returns [[0, 1], [0, 2], [1, 2], [0, 1, 2]]
    """
    # Generate masks (not the last number) for each digit
    masks = []

    for i in range(2, num_digits):
        masks.extend(itertools.combinations(range(0, num_digits - 1), i))

    return masks

start_time = time.time()

masks = {n: generate_masks(n) for n in range(5, 10)}
for num_digits, mask_list in masks.items():
    print(f"For {num_digits} digit numbers there are {len(mask_list)} masks to try")

# Now find the first one with 8
i = 56003
keep_going = True
while keep_going:
    i += 2

    if not is_prime(i):
        continue

    for mask in masks[len(str(i))]:
        p50_found, primes = p51(i, mask, 8)
        if p50_found:
            print(mask, primes, min(primes))
            keep_going = False

            break

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")