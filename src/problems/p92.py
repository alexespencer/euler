# Seems to be based on p74
import time

start_time = time.time()

def digit_square_sum(n):
    sum = 0

    for c in str(n):
        sum += int(c) ** 2

    return sum

assert digit_square_sum(44) == 32
assert digit_square_sum(32) == 13

# Chain lookup
chain_lookup = {}

def add_to_chain_lookup(n):
    if n not in chain_lookup:
        dssum = digit_square_sum(n)
        chain_lookup[n] = dssum
        if dssum not in chain_lookup:
            add_to_chain_lookup(dssum)
        return dssum
    else:
        return chain_lookup[n]

# for i in range(1, 10**7):
#     add_to_chain_lookup(i)

# Function for length of chain
def chain_length(n):
    numbers_seen = []
    while n not in numbers_seen:
        numbers_seen.append(n)
        n = add_to_chain_lookup(n)
    return len(numbers_seen), 89 in numbers_seen

count_89 = 0
for i in range(1, 10**7):
    if chain_length(i)[1]:
        count_89 += 1
print(count_89)

assert count_89==8581146

end_time = time.time()
print(f"Time taken: {end_time - start_time}")