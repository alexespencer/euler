# Print out all the 4 digit numbers that are square
import sys
import os
import time

sys.path.insert(0, os.getcwd())

from euler import HCF

# Onto something here, definitely factor based, but need to highlight similarities a bit more, maybe consider HCF between the other pair


# Find a few more, using a slow technique
def test_slow():
    odd = True
    for b in range(21, 1000):
        d = b - 1

        # Test where a is between 0.65 and 0.75 of b
        for a in range(int(b * 0.65) - 1, int(b * 0.75) + 1):
            c = a - 1
            t = b * d == 2 * a * c

            if t:
                print(f"Found bag with {b} units, of which {a} are blue")

                print("ab:", HCF(a, b))
                print("ad:", HCF(a, d))
                print("bc:", HCF(b, c))
                print("cd:", HCF(c, d))

                print("a (col 2):", HCF(a, b) * HCF(a, d))

                if odd:
                    print("b (col 1) - eve:", HCF(a, b) * HCF(b, c))
                else:
                    print("b (col 1) - odd:", (HCF(a, d) * HCF(c, d)) + 1)

                odd = not odd
                break


# test_slow()

# One of my proudest Euler moments...the HCF of a/d becomes the HCF of the NEXT item in the sequence between a/b
# And the HCF of c/b becomes the HCF of c/d
# Now we need to determine a/b from this information...
# This series is a form of Pell's number series: https://en.wikipedia.org/wiki/Pell_number
# Which is an approximation of root 2


def find_bag_50pc(limit):
    ab, ad, bc, cd = 3, 5, 7, 2
    iterations = 0
    odd = True
    while True:
        iterations += 1
        b = ab * bc if odd else ad * cd + 1

        # The block below isn't needed, but is a sanity check. Given we get to 10 ** 12 in just 15 iterations leave it in
        a = ab * ad
        c = a - 1
        d = b - 1
        assert b * d == 2 * a * c

        if b > limit:
            break

        # Next in the series
        ab = ad
        cd = bc

        if odd:
            bc = ad + bc
            ad += bc
        else:
            ad += bc
            bc += ad

        odd = not odd

    return b, a, iterations


start_time = time.time()

limit = 10**12
total_balls, blue_balls, iterations = find_bag_50pc(limit)
end_time = time.time()

print(
    f"Total time taken: {end_time - start_time:.2f} seconds. Iterations: {iterations}"
)
print("Number of items in the bag:", total_balls)
print("Number of blue items:", blue_balls)

assert total_balls * (total_balls - 1) == 2 * blue_balls * (blue_balls - 1)
