# Couting rectangles

# f(a, b) == f(b, a) = so can limit our search space

import math


def count_rectanges(x, y):
    count = 0
    for x2 in range(1, x + 1):
        for y2 in range(1, y + 1):
            count += (x - x2 + 1) * (y - y2 + 1)

    return count


assert count_rectanges(3, 2) == 18

closest = math.inf
closest_area = None
for x in range(1, 100):
    for y in range(1, 100):
        if x < y:
            continue

        r = count_rectanges(x, y)
        if abs(r - 2000000) < closest:
            closest = abs(r - 2000000)
            closest_area = x * y
            print(closest)

print(closest_area)
