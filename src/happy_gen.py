import numpy as np

HAPPY_NUMBERS_MAX_DIGITS = 10
HAPPY_NUMBERS_BASE = 10
HAPPY_NUMBERS_POWER = 2
digit_powers = np.zeros(HAPPY_NUMBERS_MAX_DIGITS + 1)
is_happy = np.zeros(HAPPY_NUMBERS_MAX_DIGITS + 1, dtype=bool)
possible_happy_number_sums = np.zeros((HAPPY_NUMBERS_MAX_DIGITS + 1, HAPPY_NUMBERS_BASE * HAPPY_NUMBERS_MAX_DIGITS, HAPPY_NUMBERS_BASE * HAPPY_NUMBERS_MAX_DIGITS), dtype=bool)
number_buffer = [''] * (HAPPY_NUMBERS_MAX_DIGITS + 1)

def isHappy(num, array_filled_to):
    if num <= array_filled_to:
        return is_happy[num]
    happy_sum = 0
    while num:
        happy_sum += digit_powers[num % HAPPY_NUMBERS_BASE]
        num //= HAPPY_NUMBERS_BASE
    return isHappy(happy_sum, array_filled_to)

def listIncrementingHappyNumbers(num_buffer, last_digit, digits_remaining, sum_remaining):
    if digits_remaining == 0:
        if sum_remaining == 0:
            num_buffer[0] = ''
            print(''.join(number_buffer))
    else:
        for digit in range(last_digit, HAPPY_NUMBERS_BASE):
            if possible_happy_number_sums[digits_remaining][sum_remaining][digit]:
                digit_powers[digits_remaining] = digit ** HAPPY_NUMBERS_POWER
                number_buffer[HAPPY_NUMBERS_MAX_DIGITS - digits_remaining] = str(digit)
                listIncrementingHappyNumbers(num_buffer, digit, digits_remaining - 1, sum_remaining - digit_powers[digits_remaining])