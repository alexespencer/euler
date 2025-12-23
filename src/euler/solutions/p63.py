# Immediate thoughts: how do we know when we can stop looking? Well, we don't need to check 10 to the power numbers...and maybe we stop if we are growing the power faster than the digits?

# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?


def find_nth_powers(x):
    numbers_found = []
    y = 0

    while True:
        y += 1
        num = x**y
        current_num_digits = len(str(num))
        if current_num_digits == y:
            numbers_found.append(num)

        if y > current_num_digits + 10:
            break
    return numbers_found


def solution() -> int:
    all_numbers_found = []
    for x in range(1, 10):
        all_numbers_found.extend(find_nth_powers(x))

    return len(set(all_numbers_found))


if __name__ == "__main__":
    print(solution())
