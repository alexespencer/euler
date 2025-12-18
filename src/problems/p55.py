import sys
import os

print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import is_palindrome, reverse_and_add


def is_lychrel(n, iter_max=50):
    """Returns if a number is a Lychrel number"""
    curr_number = n
    for i in range(iter_max):
        # Reverse and add
        curr_number = reverse_and_add(curr_number)

        # Check if palindrome
        if is_palindrome(curr_number):
            return False

    return True


# assert is_lychrel(47, 10) == True
# assert is_lychrel(349, 1) == False
# assert is_lychrel(349, 2) == False
assert not is_lychrel(349, 3)
assert is_lychrel(10677, 52)
assert not is_lychrel(10677, 53)
assert is_lychrel(196)

# # How many Lychrel numbers are there below ten-thousand? (Using 50 as a cutoff)
count = 0
for i in range(0, 10000):
    if is_lychrel(i):
        count += 1

print(count)
