from itertools import combinations


def solution_valid(cube1, cube2, squares):
    # If a 6 or 9 is in either cube, add both 6 and 9 to the set (as they can be spun around)
    cubes = [set(cube1), set(cube2)]
    for cube in cubes:
        if "6" in cube or "9" in cube:
            cube.add("6")
            cube.add("9")

    # Can each square be represented by the cubes?
    for square in squares:
        if not (
            (square[0] in cubes[0] and square[1] in cubes[1])
            or (square[0] in cubes[1] and square[1] in cubes[0])
        ):
            return False, None

    return True, cubes


def solution() -> int:
    squares = [str(i * i).zfill(2) for i in range(1, 10)]

    choices = [str(i) for i in range(10)]

    # Only 0, 1, 2, 3, 4, 5, 6, 8, 9 are used (7 is not)

    cube1 = {"0", "5", "6", "7", "8", "9"}
    cube2 = {"1", "2", "3", "4", "8", "9"}

    valid_sets = {}
    for c1 in combinations(choices, 6):
        # print(c1)
        for c2 in combinations(choices, 6):
            cube1 = frozenset(c1)
            cube2 = frozenset(c2)
            cube_ok, cubes = solution_valid(cube1, cube2, squares)
            if cube_ok:
                # Uncomment if the 6/9 should NOT count as separate
                if cube1 not in valid_sets and cube2 not in valid_sets:
                    # Neither cube is in the valid sets, so add both
                    valid_sets.setdefault(cube1, [])
                    if cube2 not in valid_sets[cube1]:
                        valid_sets[cube1].append(cube2)
                elif cube1 in valid_sets:
                    # Cube1 is in the valid sets, so add cube2 to it
                    if cube2 not in valid_sets[cube1]:
                        valid_sets[cube1].append(cube2)
                elif cube2 in valid_sets:
                    # Cube2 is in the valid sets, so add cube1 to it
                    if cube1 not in valid_sets[cube2]:
                        valid_sets[cube2].append(cube1)

    # Count the number of valid sets (unique items in the values)
    count = 0
    for v in valid_sets.values():
        count += len(v)

    return count


if __name__ == "__main__":
    print(solution())
