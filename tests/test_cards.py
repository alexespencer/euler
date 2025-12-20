import pytest

from euler.cards import canonical


class TestCards:
    def test_canonical(self):
        # Create a card
        a = canonical("TD 7H KH TS 7S".split())  # two pairs (tens and sevens)

        b = canonical("3C AH 4D 2S 5C".split())  # ace-low straight

        assert a < b

    @pytest.mark.parametrize(
        "id, hand_1, hand_2, left_wins",
        [
            ("1", "5H 5C 6S 7S KD", "2C 3S 8S 8D TD", False),  # Hand 1
            ("2", "5D 8C 9S JS AC", "2C 5C 7D 8S QH", True),  # Hand 2
            ("3", "2D 9C AS AH AC", "3D 6D 7D TD QD", False),  # Hand 3
            ("4", "4D 6S 9H QH QC", "3D 6D 7H QD QS", True),  # Hand 4
            ("5", "2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D", True),  # Hand 5
            (
                "5mod",
                "2H 2D 4C 4D 4S",
                "4C 4D 4S 9S 9D",
                False,
            ),  # Hand 5 - same three of a kind
            ("hackerrank1", "2H 3C AS 4S 5D", "2C 3S 4S 5D 6D", False),
            ("hackerrank2", "2H 3C AS 4S 5D", "6C 6S 4S 5S 6D", True),
            ("stackoverflow1", "AH 4H 4C 5H 5C", "6H 6C 7H 7C 2H", False),
            ("hackerrank1", "2H 3C AS 4S 5D", "TC JS QS KD AD", False),
        ],
    )
    def test_winning_hand(self, id, hand_1, hand_2, left_wins):
        # Create the left hand
        left_hand = canonical(hand_1.split())

        # Create the right hand
        right_hand = canonical(hand_2.split())

        # Check if the left hand wins
        assert (left_hand > right_hand) == left_wins, f"Test {id} failed"

        # When reversed, the opposite should be true
        assert (right_hand > left_hand) == (not left_wins), (
            f"Test {id} failed for reverse check"
        )
