import sys, os, time
sys.path.insert(0, os.getcwd())

from itertools import permutations
from euler import Calculation

# number_set will be a dict of Calculation -> result
# You can call Calculation.numbers_used() to get the set of numbers/digits used in all the calculation chains

if __name__ == "__main__":
    start_time = time.time()
    number_set = []

    # Populate with single digits for now
    for i in range(1, 5):
        calc = Calculation(i, None, None)
        number_set.append(calc)

    # Combine all the calcs with all the other calcs (repeat until no more calcs can be made)
    for i in range(3):
        extra_number_set = []
        for calc1 in number_set:
            for calc2 in number_set:
                if calc1 == calc2:
                    continue

                # Check if the numbers used in calc1 and calc2 are disjoint
                if calc1.numbers_used().isdisjoint(calc2.numbers_used()):
                    # Combine the two calcs using each operator
                    for operator in ["+", "-", "*", "/"]:
                        if calc2.result == 0 and operator == "/":
                            continue
                        new_calc = Calculation(calc1, operator, calc2)
                        if new_calc not in number_set:
                            extra_number_set.append(new_calc)
                            if i == 3:
                                print(f"Just added {repr(new_calc)} = {new_calc.result} using {new_calc.numbers_used()}")
                                exit()

        number_set.extend(extra_number_set)
        print(f"Added {len(extra_number_set)} calcs")

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

# print(number_set)
# for calc in number_set:
#     print(repr(calc), calc.result)

# results = [calc.result for calc in number_set]

# # Find max contigous
# i = 0
# while True:
#     i += 1
#     if i not in results:
#         print(i)
#         break