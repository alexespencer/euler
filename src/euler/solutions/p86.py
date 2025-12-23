# Thanks to a hint from mathsblog, "unfolding"/flattening the 3d shape of the cuboid makes this all a lot clearer. It's a straight line from one corner to the other where
# distance ** 2 = l ** 2 + (w + h) ** 2

# We need 1 <= h <= w <= l <= M

# We check each one for an integer solution

from euler import is_square


def solution() -> int:
    max_M = 1900
    find_n_solutions = 1000000
    count = 0
    cuboids = []
    for h in range(1, max_M + 1):
        for w in range(h, max_M + 1):
            wh_square = (w + h) ** 2
            for length in range(w, max_M + 1):
                shortest_distance_sq = (length**2) + wh_square
                if is_square(shortest_distance_sq):
                    count += 1
                    cuboids.append((h, w, length))

    if count >= find_n_solutions:
        # Find max M for which we have found n solutions
        for m in range(0, max_M + 1):
            count_found = sum([1 for cuboid in cuboids if max(cuboid) <= m])

            if count_found >= find_n_solutions:
                return m

    raise ValueError("Increase max_M limit")


if __name__ == "__main__":
    print(solution())
