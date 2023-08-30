from fractions import Fraction
from datetime import datetime
from collections import defaultdict

start_time = datetime.now()

N = 4
K = 1

def count_cancellable_digits(number1, number2):
    str_1 = str(number1)
    str_2 = str(number2)
    digits_in_common = set(str_1).intersection(set(str_2))
    return sum([min(str_1.count(digit), str_2.count(digit)) for digit in digits_in_common])

set_n = [(str(n), set(str(n)), {str(d): str(n).count(str(d)) for d in range(10)}) for n in range(10**N)]

def generate_cancellable_fractions(N, K):
    cancellable_fractions = []
    for n in range(10**(N-1), 10**N):
        for d in range(n+1, 10**N):
            digits_in_common = set_n[n][1].intersection(set_n[d][1])
            if sum([min(set_n[n][2][digit], set_n[d][2][digit]) for digit in digits_in_common]) >= K:
                cancellable_fractions.append((n, d))

    return cancellable_fractions

assert count_cancellable_digits(1234, 123) == 3
assert count_cancellable_digits(1234, 567) == 0
assert count_cancellable_digits(1234, 1234) == 4
assert count_cancellable_digits(1234, 4321) == 4
assert count_cancellable_digits(1234, 4322) == 3

start_time = datetime.now()
a = generate_cancellable_fractions(4, 1)
print(f"Time taken to generate {len(a)} fractions to consider: {datetime.now() - start_time}")
exit()
# Generate numbers without trailing zeros

numbers = {x: "".join(sorted(set(str(x)))) for x in range(10**(N-1), 10**N) if x % 10 != 0}
# digit_set_to_numbers = defaultdict(list)
# for n, digit_set in numbers.items():
#     digit_set_to_numbers[digit_set].append(n)

# Digit set intersection
# digit_set_intersection_lookup = set([digits for digits in numbers.values()])
# digit_set_intersection_lookup = {(digit_set1, digit_set2): len((set(digit_set1)).intersection(set(digit_set2))) for digit_set1 in digit_set_intersection_lookup for digit_set2 in digit_set_intersection_lookup}

# print(f"Time taken to generate intersection lookup: {datetime.now() - start_time}")

# Generate fractions, n < d and at least 1 common digit
# fractions = []
# for (digit_set1, digit_set2), intersection_count in digit_set_intersection_lookup.items():
#     if intersection_count == 0:
#         continue

#     # For the digit sets, get the numbers
#     nums1 = digit_set_to_numbers[digit_set1]
#     nums2 = digit_set_to_numbers[digit_set2]

#     fractions.extend([(n, d) for n in nums1 for d in nums2 if n < d])
fractions = [(n, d) for n in numbers for d in numbers if n < d and count_cancellable_digits(n, d) >= K]

print(f"Time taken to generate {len(fractions)} fractions to consider: {datetime.now() - start_time}")





cache = {}
def curious_fraction(n, d, k, orig_fraction=None):
    # Can we delete k digits from n/d and end up with the same fraction
    orig = Fraction(n, d)
    if orig_fraction is None:
        orig_fraction = orig
    n_digit_set = set(str(n))
    d_digit_set = set(str(d))

    # Pick a digit from the intersection
    for digit in n_digit_set.intersection(d_digit_set):
        # Get indexes of this digit
        n_digit_indexes = [i for i, x in enumerate(str(n)) if x == digit]
        d_digit_indexes = [i for i, x in enumerate(str(d)) if x == digit]
        # print(k, "Trying digit", digit, n_digit_indexes, d_digit_indexes)
        # Cartesian test

        for index1 in n_digit_indexes:
            n_new = int(str(n)[:index1] + str(n)[index1+1:])
            for index2 in d_digit_indexes:
                # Remove this index
                d_new = int(str(d)[:index2] + str(d)[index2+1:])

                if k == 1:
                    new_fraction = Fraction(n_new, d_new)
                    if new_fraction == orig_fraction:
                        return True
                else:
                    next_level = curious_fraction(n_new, d_new, k-1, orig_fraction=orig)
                    if next_level:
                        return True

    # Tried all digits, no match
    return False

assert curious_fraction(49, 98, 1) == True
assert curious_fraction(449, 494, 2) == False

assert curious_fraction(3016, 6032, 3) == True

total_n, total_d = 0, 0
for i, (n, d) in enumerate(fractions):
    if i % 10000 == 0:
        print(f"Processing {i}th fraction")
    if curious_fraction(n, d, K):
        print(f"Found curious fraction: {n}/{d}. {n/d}")
        total_n += n
        total_d += d

end_time = datetime.now()
print(f"TOTAL Duration: {end_time - start_time}.")

print(len(numbers))
print(len(fractions))
print(fractions[0:10])
print(total_n, total_d)


# 2,1 - 110 322
# 3,1 - 77262 163829
# 3,2 - 7429 17305
# 4,1 - 12999936 28131911
# 4,2 - 3571225 7153900
# 4,3 - 255983 467405