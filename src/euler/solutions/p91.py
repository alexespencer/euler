# Not the most elegant of solutions, could do with some tidying and we could also consider looking for alternative
# mathematical techniques to finding right angled triangles in a grid
# Then, we need to find all triangles where none of the coordinates are on the x or y axis


def get_all_points(limit):
    points = []
    for x in range(0, limit + 1):
        for y in range(0, limit + 1):
            points.append((x, y))
    return points


def is_right_angle_triangle(coord1, coord2):
    # Use 0,0 as the third point
    # Do (0,0), coord1 and coord2 form a right angle triangle?

    # Get the lengths of the sides
    side1 = ((coord1[0] - 0) ** 2 + (coord1[1] - 0) ** 2) ** 0.5
    side2 = ((coord2[0] - 0) ** 2 + (coord2[1] - 0) ** 2) ** 0.5
    side3 = ((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2) ** 0.5
    sides = [side1, side2, side3]
    sides.sort()
    side1, side2, side3 = sides

    # Check if the sides form a right angle triangle
    if abs((side1**2 + side2**2) - side3**2) < 0.000001:
        return True

    return False


def solution() -> int:
    limit = 50

    # There are n * n ways of getting type 1, 2 and 3 triangles
    num_triangles = limit * limit * 3

    coords = get_all_points(limit)
    all_coords = []
    for coord1 in coords:
        if coord1 == (0, 0):
            continue
        for coord2 in coords:
            if coord2 == (0, 0):
                continue
            # Remove type1/type2/type3 triangles
            # Type 1: One coord has y = 0 and one coord has x = 0
            # Type 2: One coord has y = 0 and one coord has x > 0
            # Type 3: One coord has x = 0 and one coord has y > 1

            # Type 1a
            if coord1[1] == 0 and coord2[0] == 0:
                continue
            # Type 1b
            if coord1[0] == 0 and coord2[1] == 0:
                continue

            # Type 2a
            if coord1[1] == 0 and coord2[0] > 0 and coord1[0] == coord2[0]:
                continue
            # Type 2b
            if coord1[0] > 0 and coord2[1] == 0 and coord1[0] == coord2[0]:
                continue

            # Type 3a
            if coord1[0] == 0 and coord2[1] > 0 and coord1[1] == coord2[1]:
                continue

            # Type 3b
            if coord1[1] > 0 and coord2[0] == 0 and coord1[1] == coord2[1]:
                continue

            # Use the "left" coord as the first coord
            if coord1[0] < coord2[0]:
                all_coords.append((coord1, coord2))
            elif coord1[0] > coord2[0]:
                all_coords.append((coord2, coord1))
            else:
                # If the x coords are the same, use the "lower" coord as the first coord
                if coord1[1] < coord2[1]:
                    all_coords.append((coord1, coord2))
                elif coord1[1] > coord2[1]:
                    all_coords.append((coord2, coord1))
                else:
                    # If the coords are the same, skip
                    continue

    all_coords = set(all_coords)

    # For each pair of coords, check if it's a right angle triangle
    for coord1, coord2 in all_coords:
        if is_right_angle_triangle(coord1, coord2):
            num_triangles += 1

    return num_triangles


if __name__ == "__main__":
    print(solution())
