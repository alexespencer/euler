import math


def minimal_path(matrix):
    # Insert a row of math.infs
    matrix.insert(0, [math.inf] * len(matrix[0]))

    # Also insert a column of math.infs at the beginning
    for i in range(len(matrix)):
        matrix[i].insert(0, math.inf)
    matrix[1][0] = 0  # But set the top left to 0

    # From the top down, calculate the minimum sum of the node itself and either the one above or to the left
    # Then the answer is in the bottom right node

    min_sum = 0
    for row_index in range(1, len(matrix)):
        # Get current row/previous row
        current_row = matrix[row_index]
        previous_row = matrix[row_index - 1]

        # For each column in the row...
        for col_index in range(1, len(current_row)):
            cur_node = current_row[col_index]
            left_node = current_row[col_index - 1]
            above_node = previous_row[col_index]

            # Calculate the min path
            current_row[col_index] = min(cur_node + left_node, cur_node + above_node)

            # Update the min sum (only valid on the last row)
            min_sum = current_row[-1]

    return min_sum


def solution() -> int:
    matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]

    assert minimal_path(matrix) == 2427

    # Read in the pyramid
    matrix = []
    with open("data/p81.txt", "r") as f:
        for line in f:
            matrix.append(list(map(int, line.split(","))))

    return minimal_path(matrix)


if __name__ == "__main__":
    print(solution())
