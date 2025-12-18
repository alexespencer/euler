def seq(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def longest_collatz(n):
    if n == 1:
        return 1
    elif n in collatz_length:
        return collatz_length[n]
    else:
        length = 1 + longest_collatz(seq(n))
        collatz_length[n] = length

        return length


collatz_length = {}


assert longest_collatz(1) == 1
assert longest_collatz(2) == 2
assert longest_collatz(4) == 3
assert longest_collatz(8) == 4
assert longest_collatz(13) == 10

n_to_length_lookup = {}
# length_to_n_lookup = defaultdict(list)

longest_chain = 0
for i in range(1, 5 * 10**2):
    length = longest_collatz(i)
    if length >= longest_chain:
        longest_chain = length
        n_to_length_lookup.setdefault(i, [0, set()])
        n_to_length_lookup[i][0] = length
        n_to_length_lookup[i][1].add(i)
        # length_to_n_lookup[length].append(i)

print(collatz_length)

import sys

print("Key size: ", sys.getsizeof(collatz_length))

print(n_to_length_lookup)
# print(length_to_n_lookup)


def longest_less_n(n):
    # Find the largest key in n_to_length_lookup that is less than or equal to n
    key = max([k for k in n_to_length_lookup if k <= n])

    # Now, find the max of the length_to_n_lookup[val for the key in n_to_length_lookup]
    return max(n_to_length_lookup[key][1])


assert longest_less_n(10) == 9
assert longest_less_n(15) == 9
assert longest_less_n(20) == 19

# print(longest_less_n(10 ** 6))
