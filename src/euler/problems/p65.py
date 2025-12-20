# start with numerator as 2
# Calculating the 3rd numerator

desired_nth_convergent_numerator = 100

numerator = 2
previous_numerator = 1
for i in range(2, desired_nth_convergent_numerator + 1):
    multiplier = 2 * int(i / 3) if i % 3 == 0 else 1
    previous_numerator, numerator = (
        numerator,
        previous_numerator + (numerator * multiplier),
    )  # Nifty, thanks python

print(sum(map(int, str(numerator))))  # Also nice
