
attempts = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
# De-dupe
attempts = list(set(attempts))
# Convert to arrays
attempts = [list(map(int, str(attempt))) for attempt in attempts]

attempts.insert(0, [9, 9 ,9, 9, 9, 9, 9, 9, 9, 9])

def attempt_valid(attempt, pin):
    # Attempt/pin are assumed to be ARRAYs like [3,1,9] and [3,3,3,1,1,1,9]
    # Each unique digit in attempt MUST be in the password
    if not len(set(attempt) - set(pin)) == 0:
        return False

    # Find the earliest occurence, and ensure each subsequent digit can be found AFTER
    n = -1

    for digit in attempt:
        # Try and find this digit AFTER the current n
        try:
            n = pin.index(digit, n+1)

        except ValueError:
            # Cannot be found
            return False

    return True

assert not attempt_valid([4, 1, 9], [3, 1, 9])
assert attempt_valid([3, 1, 9], [3, 1, 9])
assert not attempt_valid([3, 1, 9, 3], [3, 1, 9])
assert attempt_valid([1, 9], [3, 1, 9])
assert not attempt_valid([1, 9, 3], [3, 1, 9])
assert attempt_valid([1, 9, 3], [3, 1, 9, 3])
assert attempt_valid([1, 9, 3], [3, 1, 9, 0, 0, 0, 3])
assert attempt_valid([1, 9, 3], [3, 1, 0, 9, 0, 0, 0, 3])

assert not attempt_valid([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 1, 6])

# Brute force method, starting from a 4 digit PIN, check if each attempt would be valid
for i in range(1000000, 100000000):
    pin = [int(x) for x in str(i)]

    pin_found = all(attempt_valid(attempt, pin) for attempt in attempts)

    if pin_found:
        print(pin)
        break

    if i % 10000 == 0:
        print(i)
