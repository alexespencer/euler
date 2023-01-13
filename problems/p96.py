# P96 - Su doku
import sys, os, time
sys.path.insert(0, os.getcwd())

from sudoku import Sudoku

# Read in all sudokus
sudokus = []
with open("data/p96.txt", "r") as f:
    for line in f:
        if line.startswith("Grid"):
            # New sudoku
            sudokus.append([])
        else:
            sudokus[-1].append(line.replace('\n', ''))

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

print(f"There are {len(solved_sudokus)} solved sudokus and {len(unsolved_sudokus)} unsolved sudokus")

# Validate each soduku
sum_top_left = 0
for s in solved_sudokus:
    # Assert 1 to 9 in each row
    for row in s.grid:
        assert set(row) == set(range(1, 10))

    # Sum top left 0 to 3
    sum_top_left += int("".join(map(str, s.grid[0][0:3])))

print(f"Sum of top left: {sum_top_left}")

# Example of an unsolved sudoku
for s in unsolved_sudokus:
    print("Unsolved:")
    print(s)
    # print(s.output())

    assert 6 in s.possible_values[6][8]
    assert 9 in s.possible_values[6][8]
    print(s.find_x_wing())
    assert 6 not in s.possible_values[6][8]
    assert 9 in s.possible_values[6][8]
    s.solve()
    print(s)