# Thanks to a hint from mathsblog, "unfolding"/flattening the 3d shape of the cuboid makes this all a lot clearer. It's a straight line from one corner to the other where
# distance ** 2 = l ** 2 + (w + h) ** 2

# We need 1 <= h <= w <= l <= M

# We check each one for an integer solution

import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import is_square


max_M = 1900
find_n_solutions = 1000000
count = 0
cuboids = []
start_time = time.time()
for h in range(1, max_M + 1):
    for w in range(h, max_M + 1):
        wh_square = (w + h) ** 2
        for l in range(w, max_M + 1):
            shortest_distance_sq = (l ** 2) + wh_square
            if is_square(shortest_distance_sq):
                count += 1
                cuboids.append((h, w, l))

end_time = time.time()

print(f"M: {max_M}. count: {count}")
print(f"Time taken: {end_time - start_time:.2f} seconds")

if count >= find_n_solutions:
    # Find max M for which we have found n solutions
    for m in range(0, max_M + 1):
        count_found = sum([1 for cuboid in cuboids if max(cuboid) <= m])

        if count_found >= find_n_solutions:
            print(f"Lowest M such that the number of solutions first exceed {find_n_solutions} is {m}")
            break
else:
    print("Increase max_M limit")

