
import sys, os
sys.path.insert(0, os.getcwd())

from euler import is_square

# https://en.wikipedia.org/wiki/Periodic_continued_fraction

def continued_fraction(S):
    m = 0
    d = 1
    a0 = int(S ** 0.5)
    a = a0
    exapansion = [a]

    # The algorithm terminates when this triplet is the same as one encountered before. The algorithm can also terminate on ai when ai = 2 a0
    while True:
        m = d * a - m
        d = (S - m * m) / d

        a = int((a0 + m) / d)
        exapansion.append(a)
        if a == 2 * a0:
            break

    return exapansion

def run_test():
    test_dict = {
        1: [2, 5, 10, 17, 26, 37, 50, 65, 82, 101],
        2: [3, 6, 8, 11, 12, 15, 18, 20, 24, 27],
        3: [41, 130, 269, 370, 458],
        4: [7, 14, 23, 28, 32, 33, 34, 47, 55, 60],
        5: [13, 29, 53, 74, 85, 89, 125, 173, 185, 218],
        6: [19, 21, 22, 45, 52, 54, 57, 59, 70, 77],
        7: [58, 73, 202, 250, 274, 314, 349, 425],
        8: [31, 44, 69, 71, 91, 92, 108, 135, 153, 158],
        9: [106, 113, 137, 149, 265, 389, 493],
        10: [43, 67, 86, 93, 115, 116, 118, 129, 154]
    }
    for p, vals in test_dict.items():
        for n in vals:
            # print(n, p)
            assert len(continued_fraction(n)) - 1 == p
    print("All Tests passed")

run_test()

num_odd = 0
for n in range(2, 10000+1):
    if not is_square(n):
        period = len(continued_fraction(n)) - 1
        if period % 2 == 1:
            num_odd += 1

print(num_odd)

