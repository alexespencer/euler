import math

# Same as 81 but can start in any row on the left and end in any row on the right, plus can move up/down/right (just not left)


def minimal_path(matrix):
    # First column minimums is a copy of the first column
    mins = [row[0] for row in matrix]

    # For each column
    for i in range(1, len(matrix[0])):
        # Get the current column
        x = [row[i] for row in matrix]

        # Establish new_mins (that will overwrite mins at the end of each loop)
        new_mins = []

        for j in range(0, len(x)):
            # Left
            left = x[j] + mins[j]

            # Above
            above = min(
                [sum(x[k:j]) + mins[k] + x[j] for k in range(j - 1, -1, -1)],
                default=math.inf,
            )

            # Below
            below = min(
                [sum(x[j + 1 : k + 1]) + mins[k] + x[j] for k in range(j + 1, len(x))],
                default=math.inf,
            )

            new_mins.append(min(left, above, below))

        # Update mins
        mins = new_mins

    # Return overall minimum
    return min(mins)


def solution() -> int:
    matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    assert minimal_path(matrix) == 994

    # Read in the pyramid
    matrix = []
    with open("data/p81.txt", "r") as f:
        for line in f:
            matrix.append(list(map(int, line.split(","))))

    return minimal_path(matrix)


if __name__ == "__main__":
    print(solution())
