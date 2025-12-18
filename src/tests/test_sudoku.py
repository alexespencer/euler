
from sudoku import Sudoku

class TestSudoku:
    def test_solved(self):
        s = Sudoku(['483921657', '967345821', '251876493', '548132976', '729564138', '136798245', '372689514', '814253769', '695417382'])
        assert s.solved() == True
        assert s.grid[0][0] == 4
        assert s.grid[0][1] == 8
        assert s.grid[0][2] == 3

    def test_lock_in(self):
        s = Sudoku(['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300'])
        assert s.solved() == False
        assert s.possible_values[0][0] == [4, 5]
        assert s.possible_values[0][1] == [4, 5, 7, 8]
        assert s.grid[0][2] == 3

        # Test lock in cell, and assert possible values length is 0
        s.lock_in_cell(0, 0, 4)
        assert s.grid[0][0] == 4
        assert s.possible_values[0][0] == []

    def test_find(self):
        s = Sudoku(['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300'])
        assert s.solved() == False
        assert s.possible_values[0][0] == [4, 5]
        assert s.possible_values[0][1] == [4, 5, 7, 8]
        assert s.grid[0][2] == 3

        s.lock_in_cell(0, 0, 4)

        print(s.find_single())
        assert s.grid[8] == [6, 9, 5, 4, 1, 7, 3, 8, 2]

        print(s.find_hidden_single())
        assert s.grid[3] == [5, None, 8, 1, 3, 2, 9, 7, 6]

    def test_solve(self):
        s = Sudoku(['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300'])
        s.solve()
        assert s.solved() == True

    def test_find_locked_candidates1(self):
        s = Sudoku(['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300'])
        s.solve()
        assert s.solved() == True

        s = Sudoku(['801007090', '590080061', '030000080', '010275843', '358060127', '274138956', '080000030', '100820079', '020700418'])
        # Run find_locked_candidates() until it returns False
        while s.find_locked_candidates():
            pass

        assert 4 not in s.possible_values[0][3]
        assert 4 not in s.possible_values[0][4]
        assert 4 not in s.possible_values[2][3]
        assert 4 not in s.possible_values[2][4]
        assert 4 not in s.possible_values[2][5]


    def test_find_locked_candidates2(self):
        s = Sudoku(['003020600','900305001','000806400','008002900','700000008','006708200','002609500','800203009','005010300'])
        print(s)
        assert 1 in s.possible_values[0][0]
        print(s.find_locked_candidates())
        assert 1 not in s.possible_values[0][0]

    def test_find_naked_pairs_row(self):
        s = Sudoku(['000000000', '967345820', '251876403', '548032976', '729564138', '136708245', '372680514', '814253760', '695007382'])
        print(s.output())
        print(s)
        print(s.possible_values[0][3:6])
        assert s.possible_values[0][3:6] == [[1, 9], [1, 2, 9], [1, 9]]
        assert 1 in s.possible_values[0][8]
        assert 9 in s.possible_values[0][8]
        print(s.find_naked_pairs())
        assert 1 not in s.possible_values[0][8]
        assert 9 not in s.possible_values[0][8]

    def test_find_naked_pairs_column(self):
        s = Sudoku(['683175290', '917324560', '542698170', '026750830', '058063740', '730842650', '375219480', '861437020', '204586300'])
        print(s)
        print(s.possible_values[0][3:6])
        assert s.possible_values[3][-1] == [1, 9]
        assert s.possible_values[4][-1] == [1, 2, 9]
        assert s.possible_values[5][-1] == [1, 9]

        assert 1 in s.possible_values[8][8]
        assert 9 in s.possible_values[8][8]
        print(s.find_naked_pairs())
        assert 1 not in s.possible_values[8][8]
        assert 9 not in s.possible_values[8][8]

    # def test_find_naked_pairs_box(self):
    #     # Need to manually disable row/col fix for now
    #     s = Sudoku(['000000000', '967345820', '251876403', '548032976', '729564138', '136708245', '372680514', '814253760', '695007382'])
    #     print(s)
    #     # assert False is True
    #     # Force a possible 1
    #     s.possible_values[2][3].append(1)
    #     assert 1 in s.possible_values[2][3]

    #     print(s.find_naked_pairs())
    #     assert 1 not in s.possible_values[2][3]

    # def test_find_hidden_n(self):
    # TODO: Find a soduku that this test works on
    #     s = Sudoku(['000003017','015009038','063000002','100007000','009006200','000502004','000000020','500600340','340200000'])

    #     # Run solve without hidden, then assert it removes possible values
    #     updated = True
    #     while updated:
    #         updated = False
    #         updated = s.find_single() or updated
    #         updated = s.find_hidden_single() or updated
    #         updated = s.find_locked_candidates() or updated
    #         updated = s.find_naked_pairs() or updated

    #     assert s.solved() == False
    #     print(s.possible_values)
    #     print(s.possible_values[0][4])
    #     assert 2 in s.possible_values[0][4]
    #     assert 8 in s.possible_values[0][4]
    #     assert 4 in s.possible_values[0][6]
    #     assert 9 in s.possible_values[0][6]

    #     assert s.find_hidden_n() == True

    #     assert 2 not in s.possible_values[0][4]
    #     assert 8 not in s.possible_values[0][4]
    #     assert 4 not in s.possible_values[0][6]
    #     assert 9 not in s.possible_values[0][6]

    def test_column_possible_values(self):
        s = Sudoku(['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300'])
        assert s.solved() == False
        assert s.possible_values[0][0] == [4, 5]
        assert s.possible_values[0][1] == [4, 5, 7, 8]
        assert s.grid[0][2] == 3

        assert s.column_possible_values()[0][0] == [4, 5]
        assert s.column_possible_values()[1][0] == [4, 5, 7, 8]

        for col in range(9):
            for row in range(9):
                assert s.column_possible_values()[col][row] == s.possible_values[row][col]

