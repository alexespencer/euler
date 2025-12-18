from math import factorial

factorial_cache = {}
for i in range(0, 10):
    factorial_cache[str(i)] = factorial(i)

print(factorial_cache)

def digit_factorial_sum(n):
    sum = 0

    for c in str(n):
        sum += factorial_cache[c]

    return sum

assert digit_factorial_sum(145) == 145
assert digit_factorial_sum(69) == 363600

# Chain lookup
chain_lookup = {}

def add_to_chain_lookup(n):
    dfs = digit_factorial_sum(n)
    if n not in chain_lookup:
        chain_lookup[n] = dfs
        if dfs not in chain_lookup:
            add_to_chain_lookup(dfs)

for i in range(1, 10**6):
    add_to_chain_lookup(i)

# We

# Function for length of chain
def chain_length(n):
    numbers_seen = []
    while n not in numbers_seen:
        numbers_seen.append(n)
        n = chain_lookup[n]
    return len(numbers_seen)

assert chain_length(69) == 5
assert chain_length(78) == 4
assert chain_length(540) == 2
assert chain_length(145) == 1

# Count how many numbers <= 10**6 have a chain length of exactly 60
# We could make this faster by caching the chain length of each sub chain - so if the number is encountered again, we can skip the rest of the chain
count = 0
for i in range(1, 10**6):
    if chain_length(i) == 60:
        count += 1
print(count)