# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def p52(number, multiplies=[2, 3, 4, 5, 6]):
    num_digit_set = sorted(list(str(number)))
    for m in multiplies:
        if num_digit_set != sorted(list(str(number * m))):
            return False

    return True

assert p52(125874, [2]) == True

found = False
i = 0
while not found:
    i += 1

    if p52(i):
        print(i)
        found = True