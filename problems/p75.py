import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import is_square

triangles = {}

# The area of a right angled triangles with integer sides is always divisible by 3 

max_length = 150000
for a in range(3, max_length // 3):
    if a % 10000 == 0:
        print(a)
    
    for b in range(a+1, max_length // 3):
        if (a * b) / 2 % 3 == 0:
            # Determine length
            c = (a ** 2 + b ** 2)

            if not is_square(c):
                continue

            length = int(a + b + (c ** 0.5))
            if length > max_length:
                break

            triangles.setdefault(length, [])
            if (a, b, c) not in triangles[length]:
                triangles[length].append((a, b, c))

count = 0
for length, triangles in triangles.items():
    if len(triangles) == 1 and length <= max_length:
        count += 1
        # print(length, triangles)
print(count)
