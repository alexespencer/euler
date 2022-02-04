from http.client import ImproperConnectionState
import pytest

from euler import pentagon_n, quadratic_equation, is_pentagon_number

class TestBlob:
    def test_pentagon(self):
        # Test pengtagon numbers
        assert list(map(pentagon_n, range(1, 11))) == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        assert all([is_pentagon_number(n) for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]])
        assert all([is_pentagon_number(n + 1) == False for n in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]])

    @pytest.mark.parametrize("a, b, c, p1, p2",
                                [(1, -3, 2, 2, 1),
                                (1, 5, 6, -2, -3),
                                (3, -6, 3, 1, 1),
                                (-3, -24, -48, -4, -4),
                                (1, 2, 0, 0, -2)])
    def test_quad_no_error(self, a, b, c, p1, p2):
        assert quadratic_equation(a, b, c) == (p1, p2)

    def test_quad_error(self):
        with pytest.raises(ValueError) as e_info:
            quadratic_equation(2, -4, 7)
