# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

results = []
for a in range(2, 100):
    for b in range(2, 100):
        num = a**b
        # Sum digits in num
        sum_digits = sum([int(char) for char in str(num)])
        results.append((sum_digits, a, b))

# Sort results by descending first element
results.sort(key=lambda x: x[0], reverse=True)
print(results[0:10])
