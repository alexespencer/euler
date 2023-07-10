class Sumplete:
    def __init__(self, row_count, col_count):
        self.grid = [[0 for _ in range(col_count)] for _ in range(row_count)]
        self.row_count = row_count
        self.col_count = col_count

        # Initialise with 0s the row/col totals
        self.row_totals = [0 for _ in range(row_count)]
        self.col_totals = [0 for _ in range(col_count)]

    def __str__(self):
        temp_str = ""

        for row, row_total in zip(self.grid, self.row_totals):
            temp_str += "  ".join(map(str, row)) + f" | {row_total}\n"

        temp_str += f"{'-' * (self.col_count * 3)}\n"

        temp_str += " ".join(map(str, self.col_totals))

        return temp_str
    
    @staticmethod
    def from_strings(rows, col_totals):
        # Rows will be like ["12345,10", "12301,4"...]
        # Col_totals will be like "2,4,6,8,10"

        # First, parse the rows
        row_count = len(rows)
        col_count = len(rows[0].split(",")[0])

        sumplete = Sumplete(row_count, col_count)

        for i, row in enumerate(rows):
            row = row.split(",")
            for j, cell in enumerate(row[0]):
                sumplete.grid[i][j] = int(cell)
            
            # Next, parse the row_totals
            sumplete.row_totals[i] = int(row[1])

        # Next, parse the col_totals
        sumplete.col_totals = list(map(int, col_totals.split(",")))

        return sumplete
    

sumplete = Sumplete.from_strings(["4935766,15", "3344583,11", "2236373,19", "1425719,20", "9627372,19", "9724727,22", "9757136,13"], "16,23,10,20,14,24,12")

print(sumplete)