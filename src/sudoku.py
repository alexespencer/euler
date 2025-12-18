
class Sudoku:
    def __init__(self, nine_lines):
        # nine_lines is a list of nine strings, each string is a row of the sudoku
        self.grid = []
        self.possible_values = []
        for line in nine_lines:
            self.grid.append([x for x in list(map(int, line))])
            self.possible_values.append([[] for i in range(0, 9)])

        # Replace 0s with None and update the list of possible values
        for row_index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell == 0:
                    self.grid[row_index][cell_index] = None
                    self.possible_values[row_index][cell_index] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # First init, we need to lock in all single values
        for row_index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell:
                    self.lock_in_cell(row_index, cell_index, cell)

    def find_single(self):
        # Find a single value in a row
        updated = False
        for row_index, row in enumerate(self.possible_values):
            for cell_index, cell in enumerate(row):
                if len(cell) == 1:
                    self.lock_in_cell(row_index, cell_index, cell[0])
                    updated = True

        # Find a single value in a column
        for col_index, col in enumerate(self.column_possible_values()):
            for row_index, cell in enumerate(col):
                if len(cell) == 1:
                    self.lock_in_cell(row_index, col_index, cell[0])
                    updated = True

        # Find a single value in a 3x3 box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                box = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        box.append(self.possible_values[i][j])

                for cell_index, cell in enumerate(box):
                    if len(cell) == 1:
                        # Convert cell_index to row and col
                        row = box_row * 3 + cell_index // 3
                        col = box_col * 3 + cell_index % 3
                        self.lock_in_cell(row, col, cell[0])
                        updated = True

        return updated

    def find_hidden_single(self):
        """Hidden single is when in a row, column or 3x3 box, there is only one place a number can go"""
        updated = False
        # Find hidden single in a row
        for row_index, row in enumerate(self.possible_values):
            for value in range(1, 10):
                # Find the number of cells that can contain the value
                cells = [i for i, cell in enumerate(row) if value in cell]
                if len(cells) == 1:
                    self.lock_in_cell(row_index, cells[0], value)
                    updated = True

        # Find hidden single in a column
        for col_index, col in enumerate(self.column_possible_values()):
            for value in range(1, 10):
                # Find the number of cells that can contain the value
                cells = [i for i, cell in enumerate(col) if value in cell]
                if len(cells) == 1:
                    self.lock_in_cell(cells[0], col_index, value)
                    updated = True

        # Find hidden single in a 3x3 box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                box = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        box.append(self.possible_values[i][j])

                for value in range(1, 10):
                    # Find the number of cells that can contain the value
                    cells = [i for i, cell in enumerate(box) if value in cell]
                    if len(cells) == 1:
                        # Convert cell_index to row and col
                        row = box_row * 3 + cells[0] // 3
                        col = box_col * 3 + cells[0] % 3
                        self.lock_in_cell(row, col, value)
                        updated = True

        return updated

    def lock_in_cell(self, update_row, update_col, value):
        # Lock in a value for a cell
        self.grid[update_row][update_col] = value
        self.possible_values[update_row][update_col] = []

        # Remove the value from the row possible values
        for cell_index, cell in enumerate(self.possible_values[update_row]):
            if value in cell:
                self.possible_values[update_row][cell_index].remove(value)

        # Remove the value from the column
        for row_index, row in enumerate(self.possible_values):
            if value in row[update_col]:
                self.possible_values[row_index][update_col].remove(value)

        # Remove the value from the 3x3 box
        # Find the top left corner of the box
        box_row = update_row // 3 * 3
        box_col = update_col // 3 * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if value in self.possible_values[i][j]:
                    self.possible_values[i][j].remove(value)

    def solved(self):
        # Solved if all cells are length 1
        for row in self.grid:
            for cell in row:
                if not cell:
                    return False

        return True

    def solve(self):
        updated = True
        while updated:
            updated = False
            updated = self.find_single() or updated
            updated = self.find_hidden_single() or updated
            updated = self.find_locked_candidates() or updated
            updated = self.find_naked_pairs() or updated
            updated = self.find_hidden_n() or updated
            updated = self.find_x_wing() or updated

    def find_locked_candidates(self):
        """Locked candidates is when a value can only be in a row or column in a 3x3 box"""
        updated = False

        # Type 1 (pointing)
        # Find locked candidates in a box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                for value in range(1, 10):
                    box = []
                    for i in range(box_row * 3, box_row * 3 + 3):
                        for j in range(box_col * 3, box_col * 3 + 3):
                            if value in self.possible_values[i][j]:
                                box.append((i, j))

                    # Check if cols are the same
                    if len(box) > 1 and len(set([col for row, col in box])) == 1:
                        # Remove value from the other boxes in the col
                        col = box[0][1]
                        for i in range(0, 9):
                            if i // 3 != box_row and value in self.possible_values[i][col]:
                                self.possible_values[i][col].remove(value)
                                updated = True

                    # Check if rows are the same
                    if len(box) > 1 and len(set([row for row, col in box])) == 1:
                        # Remove value from the other boxes in the row
                        row = box[0][0]
                        for j in range(0, 9):
                            if j // 3 != box_col and value in self.possible_values[row][j]:
                                self.possible_values[row][j].remove(value)
                                updated = True

        # Type 2 (claiming)
        # Find locked candidates in a row
        for row_index, row in enumerate(self.possible_values):
            # if row_index == 1:
                # print(row_index, row)
            for value in range(1, 10):
                # For the current row, cells contains the column indexes of the cells that CAN contain the value
                cells = [i for i, cell in enumerate(row) if value in cell]

                # if row_index == 1 and value == 4 and cells == [3, 5]:
                #     print(cells)
                #     pass

                if len(cells) > 1 and len(set([col // 3 for col in cells])) == 1:
                    # Remove value from all other cells in the box
                    box_col = cells[0] // 3
                    box_row = row_index // 3

                    # Remove value from all other cells in this box
                    for i in range(box_row * 3, box_row * 3 + 3):
                        for j in range(box_col * 3, box_col * 3 + 3):
                            if not (i == row_index and j in cells) and value in self.possible_values[i][j]:
                                self.possible_values[i][j].remove(value)
                                updated = True


        # Find locked candidates in a column
        for col_index, col in enumerate(self.column_possible_values()):
            for value in range(1, 10):
                # For the current col, cells contains the row indexes of the cells that CAN contain the value
                cells = [i for i, cell in enumerate(col) if value in cell]

                if len(cells) > 1 and len(set([row // 3 for row in cells])) == 1:
                    # Remove value from all other cells in the box
                    box_row = cells[0] // 3
                    box_col = col_index // 3

                    # Remove value from all other cells in this box
                    for i in range(box_row * 3, box_row * 3 + 3):
                        for j in range(box_col * 3, box_col * 3 + 3):
                            if not (j == col_index and i in cells) and value in self.possible_values[i][j]:
                                self.possible_values[i][j].remove(value)
                                updated = True

        return updated

    def find_x_wing(self):
        """Two cells in a row or column, which together contain only the same two candidates. These candidates can be excluded from other cells in the same row or column."""
        updated = False

        # Very similar to our hidden pairs
        # Find x-wing in a row
        lookup = {} # Will be value: [row_index, [candidates]]

        for row_index, row in enumerate(self.possible_values):
            for value in range(1, 10):
                cells = [i for i, cell in enumerate(row) if value in cell]
                if len(cells) == 2:
                    lookup.setdefault(value, []).append((row_index, cells))

        # For each value, if there are 2 rows with the same 2 candidates, remove the value from the other cells in the row
        for value, row_candidates in lookup.items():
            group_lookup = {}
            for row_index, col_indexes in row_candidates:
                group_lookup.setdefault(frozenset(col_indexes), []).append(row_index)

            # Go through group_lookup and find where length of value/value is the same
            for col_indexes, row_indexes in group_lookup.items():
                if len(row_indexes) == 2 and len(col_indexes) == 2:
                    # print(f"Found xwing in row {row_indexes} for value {value} - removing from other cells in columns {list(col_indexes)}")
                    # Remove value from other cells in the column
                    for col_index in col_indexes:
                        for row_index in range(0, 9):
                            if row_index not in row_indexes and value in self.possible_values[row_index][col_index]:
                                # print(f"Removing {value} from {row_index}, {col_index}")
                                self.possible_values[row_index][col_index].remove(value)
                                updated = True

        # Find x-wing in a column
        lookup = {} # Will be value: [col_index, [candidates]]

        for col_index, col in enumerate(self.column_possible_values()):
            for value in range(1, 10):
                cells = [i for i, cell in enumerate(col) if value in cell]
                if len(cells) == 2:
                    lookup.setdefault(value, []).append((col_index, cells))

        # For each value, if there are 2 columns with the same 2 candidates, remove the value from the other cells in the column
        for value, col_candidates in lookup.items():
            group_lookup = {}
            for col_index, row_indexes in col_candidates:
                group_lookup.setdefault(frozenset(row_indexes), []).append(col_index)

            # Go through group_lookup and find where length of value/value is the same
            for row_indexes, col_indexes in group_lookup.items():
                if len(col_indexes) == 2 and len(row_indexes) == 2:
                    # print(f"Found xwing in col {col_indexes} for value {value} - removing from other cells in rows {list(row_indexes)}")
                    # Remove value from other cells in the column
                    for row_index in row_indexes:
                        for col_index in range(0, 9):
                            if col_index not in col_indexes and value in self.possible_values[row_index][col_index]:
                                # print(f"Removing {value} from {row_index}, {col_index}")
                                self.possible_values[row_index][col_index].remove(value)
                                updated = True

        return updated

    def find_naked_pairs(self):
        """Two cells in a row, column or block, which together contain only the same two candidates. These candidates can be excluded from other cells in the same row, column or block."""
        updated = False

        # Find naked pairs in a row
        for row_index, row in enumerate(self.possible_values):
            # Get cells with 2 possible values
            cells = [[cell_index, frozenset(possible_values)] for cell_index, possible_values in enumerate(row) if len(possible_values) == 2]
            if len(cells) > 1:
                # Group by 2nd element (the frozenset)
                groups = {}
                for column_index, candidates in cells:
                    groups.setdefault(candidates, []).append(column_index)

                # For each group, if there are 2 cells, remove the candidates from the other cells in the row
                for candidates, columns in groups.items():
                    if len(columns) == 2:
                        for cell_index, cell in enumerate(row):
                            if cell_index not in columns:
                                for value in candidates:
                                    if value in cell:
                                        self.possible_values[row_index][cell_index].remove(value)
                                        updated = True

        # Find naked pairs in a column
        for col_index, col in enumerate(self.column_possible_values()):
            # Get cells with 2 values
            cells = [[row_index, frozenset(possible_values)]
                        for row_index, possible_values in enumerate(col)
                        if len(possible_values) == 2]
            if len(cells) > 1:
                # Group by 2nd element (the frozenset)
                groups = {}
                for row_index, candidates in cells:
                    groups.setdefault(candidates, []).append(row_index)

                # For each group, if there are 2 cells, remove the candidates from the other cells in the row
                for candidates, rows in groups.items():
                    if len(rows) == 2:
                        for row_index, row in enumerate(self.possible_values):
                            if row_index not in rows:
                                for value in candidates:
                                    if value in row[col_index]:
                                        self.possible_values[row_index][col_index].remove(value)
                                        updated = True

        # Find naked pairs in a box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                # Get cells with 2 values
                box = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        box.append((i, j, self.possible_values[i][j]))

                cells = [[row_index, col_index, frozenset(possible_values)] for row_index, col_index, possible_values in box if len(possible_values) == 2]

                if len(cells) > 1:
                    # Group by 2nd element (the frozenset)
                    groups = {}
                    for row_index, col_index, candidates in cells:
                        groups.setdefault(candidates, []).append((row_index, col_index))

                    # For each group, if there are 2 cells, remove the candidates from the other cells in the box
                    for candidates, cells in groups.items():
                        if len(cells) == 2:

                            for row_index, col_index, _ in box:
                                if (row_index, col_index) not in cells:
                                    for value in candidates:
                                        if value in self.possible_values[row_index][col_index]:
                                            self.possible_values[row_index][col_index].remove(value)
                                            updated = True

        return updated

    def column_possible_values(self):
        return [[row[col_index] for row in self.possible_values] for col_index in range(0, 9) ]

    def find_hidden_n(self):
        """Two (or 3 or 4) candidates that appear only in two cells in a row, column or block. Other candidates in those two cells can be eliminated"""
        updated = False

        # Find hidden pairs in a row
        for row_index, row in enumerate(self.possible_values):
            lookup = {} # Value: [col_indexes]

            # Then, if there are n values in the same n cells, remove other candidates from these cells
            for col_index, possible_values in enumerate(row):
                for value in possible_values:
                    lookup.setdefault(value, []).append(col_index)

            grouped_lookup = {}
            for value, col_indexes in lookup.items():
                grouped_lookup.setdefault(frozenset(col_indexes), []).append(value)

            # If any items has the same number of values as it does keys, print it
            for col_indexes, values in grouped_lookup.items():
                if len(col_indexes) == len(values):
                    # print(f"On row {row_index} there is a hidden group of {len(values)}, values are {values}, in columns {list(col_indexes)}")
                    # Remove other candidates from these cells
                    for col_index in col_indexes:
                        for value in row[col_index]:
                            if value not in values:
                                # print(f"Removing {value} from {row_index}, {col_index}")
                                self.possible_values[row_index][col_index].remove(value)
                                updated = True

        # Find hidden pairs in a column
        for col_index, col in enumerate(self.column_possible_values()):
            lookup = {}

            # Then, if there are n values in the same n cells, remove other candidates from these cells
            for row_index, possible_values in enumerate(col):
                for value in possible_values:
                    lookup.setdefault(value, []).append(row_index)

            grouped_lookup = {}
            for value, row_indexes in lookup.items():
                grouped_lookup.setdefault(frozenset(row_indexes), []).append(value)

            # If any items has the same number of values as it does keys, print it
            for row_indexes, values in grouped_lookup.items():
                if len(row_indexes) == len(values):
                    # print(f"On column {col_index} there is a hidden group of {len(values)}, values are {values}, in rows {list(row_indexes)}")
                    # Remove other candidates from these cells
                    for row_index in row_indexes:
                        for value in self.possible_values[row_index][col_index]:
                            if value not in values:
                                # print(f"Removing {value} from {row_index}, {col_index}")
                                self.possible_values[row_index][col_index].remove(value)
                                updated = True

        # Find hidden pairs in a box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                # Get cells with 2 values
                box = []
                for i in range(box_row * 3, box_row * 3 + 3):
                    for j in range(box_col * 3, box_col * 3 + 3):
                        box.append((i, j, self.possible_values[i][j]))

                lookup = {}

                # Then, if there are n values in the same n cells, remove other candidates from these cells
                for row_index, col_index, possible_values in box:
                    for value in possible_values:
                        lookup.setdefault(value, []).append((row_index, col_index))

                grouped_lookup = {}
                for value, cells in lookup.items():
                    grouped_lookup.setdefault(frozenset(cells), []).append(value)

                # If any items has the same number of values as it does keys, print it
                for cells, values in grouped_lookup.items():
                    if len(cells) == len(values):
                        # print(f"On box {box_row}, {box_col} there is a hidden group of {len(values)}, values are {values}, in cells {list(cells)}")
                        # Remove other candidates from these cells
                        for row_index, col_index in cells:
                            for value in self.possible_values[row_index][col_index]:
                                if value not in values:
                                    # print(f"Removing {value} from {row_index}, {col_index}")
                                    self.possible_values[row_index][col_index].remove(value)
                                    updated = True

        return updated

    def output(self):
        out = ''
        for row in self.grid:
            for cell in row:
                out += str(cell if cell else 0)
            out += "\n"
        return out

    def __repr__(self):
        # Print the grid
        out = ''

        for row_index, row in enumerate(self.grid):
            if row_index % 3 == 0:
                out += '-------------------------\n'

            for col_index, cell in enumerate(row):
                if col_index % 3 == 0:
                    out += '| '
                if cell:
                    out += str(cell) + ' '
                else:
                    out += '  '
            out += '|\n'
        out += '-------------------------\n'
        return out
