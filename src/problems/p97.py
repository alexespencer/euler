# Find the last ten digits of this prime number: 28433 * (2 ** 7830457) + 1
from time import time

# Can we just keep the last 10 digits (throwing away the rest) and multiply by 2 each time, up to the required n?

def p97(mult, base, power, digits=10):
    x = mult

    for _ in range(power):
        x = x * base

        # Now limit x to the last 10 digits
        x = x % (10 ** digits)

    return x

assert p97(2354, 2, 60) + 1 == int((str(2354 * (2 ** 60)))[-10:]) + 1

print("Calculating...")
start_time = time()
answer = p97(28433, 2, 7830457) + 1
end_time = time()
print(str(answer)[-10:])
print(f"Time taken: {(end_time - start_time):.2f}")