import time
from itertools import permutations, product

# Previous WIP would have taken 4 hours, not good enogh

start_time = time.time()

digit_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def possible_calculations(digits):
    # All combinations of the digits
    all_numbers = []
    for a, b, c, d in permutations(digits, 4):
        # All combinations of the operators
        for op1, op2, op3 in product("+-*/", repeat=3):
            # All combinations of the brackets
            fs = [
                " ".join(["(", str(a), op1, str(b), ")", op2, str(c), op3, str(d)]),
                " ".join([str(a), op1, "(", str(b), op2, str(c), ")", op3, str(d)]),
                " ".join([str(a), op1, str(b), op2, "(", str(c), op3, str(d), ")"]),
                " ".join(["(", str(a), op1, str(b), op2, str(c), ")", op3, str(d)]),
                " ".join([str(a), op1, "(", str(b), op2, str(c), op3, str(d), ")"]),
            ]

            for f in fs:
                try:
                    r = eval(f)

                    if int(r) == r and r > 0 and r not in all_numbers:
                        all_numbers.append(r)
                except Exception:
                    pass

    return all_numbers


# Generate all the permutations of the digits
longest_run = 0
longest_run_digits = None
for perm in permutations(digit_set, 4):
    a, b, c, d = perm
    if a < b < c < d:
        all_numbers = possible_calculations(list(perm))
        all_numbers.sort()

        # Find the first number that is not in the list
        for i in range(1, len(all_numbers)):
            if all_numbers[i] != i + 1:
                # print(i)
                if i > longest_run:
                    longest_run = i
                    longest_run_digits = perm

                break

print(longest_run, longest_run_digits)
