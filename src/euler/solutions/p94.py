from euler import fast_pythag_triples


def solution() -> int:
    max_perimeter = 1000000000
    max_length_side = (max_perimeter // 3) + 2

    # For each triple, see if it forms an almost equilateral triangle
    almost_equilateral = set()

    for triple in fast_pythag_triples(max_length_side):
        a, b, c = triple
        # If the absolute difference between 2a and c is 1, we have found an AET
        if abs(2 * a - c) == 1:
            almost_equilateral.add(tuple([c, c, 2 * a]))
        if abs(2 * b - c) == 1:
            almost_equilateral.add(tuple([c, c, 2 * b]))

    # Sum the perimeter of all AETs
    sum_perimeter = sum([sum(triple) for triple in almost_equilateral])
    return sum_perimeter


if __name__ == "__main__":
    print(solution())
