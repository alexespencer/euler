from euler.primes import phi


def test_phi():
    assert phi(2) == 1
    assert phi(3) == 2
    assert phi(4) == 2
    assert phi(5) == 4
    assert phi(6) == 2
    assert phi(7) == 6
    assert phi(8) == 4
    assert phi(9) == 6
    assert phi(10) == 4
