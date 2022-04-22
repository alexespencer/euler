from math import factorial

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

assert combinations(5, 3) == 10
assert combinations(23, 10) == 1144066

greater_1m = 0
for n in range(23, 101):
    for r in range(2, 101):
        if r > n:
            continue

        if combinations(n, r) > 1000000:
            greater_1m += 1

print(greater_1m)