import os
import sys

print(f"Adding to path: {os.getcwd()}")
sys.path.insert(0, os.getcwd())

from euler import is_pentagon_number, pentagon_n

# See if we can find ANY pair
for j in range(1, 3000):
    n1_p = pentagon_n(j)

    for k in range(j + 1, 3000):
        n2_p = pentagon_n(k)

        if is_pentagon_number(n1_p + n2_p) and is_pentagon_number(n2_p - n1_p):
            print(j, k, n2_p - n1_p)
