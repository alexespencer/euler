from euler.problems.p69 import phi


def test_phi():
    factor_sets = {}

    assert phi(2, factor_sets) == 1
    assert phi(3, factor_sets) == 2
    assert phi(4, factor_sets) == 2
    assert phi(5, factor_sets) == 4
    assert phi(6, factor_sets) == 2
    assert phi(7, factor_sets) == 6
    assert phi(8, factor_sets) == 4
    assert phi(9, factor_sets) == 6
    assert phi(10, factor_sets) == 4
