# Immediate thoughts: how do we know when we can stop looking? Well, we don't need to check 10 the the power numbers...and maybe we stop if we are growning the power faster than the digits?

# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

def find_nth_powers(x):
    print("Finding nth powers of", x)
    numbers_found = []
    y = 0

    while True:
        y += 1
        num = x**y
        current_num_digits = len(str(num))
        if current_num_digits == y:
            numbers_found.append(num)
            print(f"Found {x**y} which is a {len(str(x**y))} digit number and a {y}th power ({x} to the power of {y})")


        if y > current_num_digits + 10:
            print("Stopping because we can't find any more")
            print(f"Stopping where power was {y} and we were seeing {current_num_digits} digits and the num was {num}")

            break
    return numbers_found

all_numbers_found = []
for x in range(1, 10):
    all_numbers_found.extend(find_nth_powers(x))

print(len(all_numbers_found))
print(len(set(all_numbers_found)))