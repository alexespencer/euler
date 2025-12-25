# P96 - Sudoku
from euler.sudoku import Sudoku


def solution() -> int:
    # Read in all sudokus
    sudokus = []
    with open("data/p96.txt", "r") as f:
        for line in f:
            if line.startswith("Grid"):
                # New sudoku
                sudokus.append([])
            else:
                sudokus[-1].append(line.replace("\n", ""))

    sudokus = [Sudoku(sudoku) for sudoku in sudokus]

    # Apply our solver, we may not get a solution for all sudokus
    solved_sudokus = []
    unsolved_sudokus = []
    for sudoku in sudokus:
        sudoku.solve()
        if sudoku.solved():
            solved_sudokus.append(sudoku)
        else:
            unsolved_sudokus.append(sudoku)

    # Validate each soduku
    sum_top_left = 0
    for s in solved_sudokus:
        # Assert 1 to 9 in each row
        for row in s.grid:
            assert set(row) == set(range(1, 10))

        # Sum top left 0 to 3
        sum_top_left += int("".join(map(str, s.grid[0][0:3])))

    return sum_top_left


if __name__ == "__main__":
    print(solution())
