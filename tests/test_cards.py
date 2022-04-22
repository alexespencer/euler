
import pytest

from problems.cards import Card, Hand, RankedHand

class TestCards:
    def test_str_repr(self):
        # Create a card
        card = Card('C', 'A')
        assert str(card) == 'Ace of Clubs'
        assert repr(card) == 'Card(suit=\'C\', rank=\'A\')'

    def test_hand_royal_flush(self):
        # Create a hand
        cards = [Card('C', 'A'), Card('C', 'K'), Card('C', 'Q'), Card('C', 'J'), Card('C', 'T')]
        hand = Hand(cards)
        assert hand.royal_flush() == RankedHand('Royal Flush', 14, [0, 1, 2, 3, 4])
        assert hand.straight_flush() == RankedHand('Straight Flush', 14, [0, 1, 2, 3, 4])

        # Reverse the cards and try again
        cards.reverse()
        hand = Hand(cards)
        assert hand.royal_flush() == RankedHand('Royal Flush', 14, [0, 1, 2, 3, 4])

        # Create a hand
        cards = [Card('C', '2'), Card('C', 'K'), Card('C', 'Q'), Card('C', 'J'), Card('C', 'T')]
        hand = Hand(cards)
        assert hand.royal_flush() == None

    def test_hand_straight_flush(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.straight_flush() == RankedHand('Straight Flush', 6, [0, 1, 2, 3, 4])
        assert hand.straight() == RankedHand('Straight', 6, [0, 1, 2, 3, 4])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '8'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.straight_flush() == None

    def test_four_of_a_kind(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '2'), Card('C', '2'), Card('C', '2'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.four_of_a_kind() == RankedHand('Four of a Kind', 2, [0, 1, 2, 3])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '2'), Card('C', '2'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.four_of_a_kind() == None

    def test_full_house(self):
        # Create a hand
        cards = [Card('H', '2'), Card('D', '2'), Card('C', '4'), Card('D', '4'), Card('S', '4')]
        hand = Hand(cards)
        assert hand.full_house() == RankedHand('Full House', 4, [2, 3, 4])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '2'), Card('C', '6'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.full_house() == None

    def test_flush(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.flush() == RankedHand('Flush', 6, [0, 1, 2, 3, 4])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('D', '8'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.flush() == None

    def test_straight(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '4'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.straight() == RankedHand('Straight', 6, [0, 1, 2, 3, 4])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '8'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.straight() == None

    def test_three_of_a_kind(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '2'), Card('C', '2'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.three_of_a_kind() == RankedHand('Three of a Kind', 2, [0, 1, 2])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '2'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.three_of_a_kind() == None

    def test_two_pair(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '2'), Card('C', '5'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.two_pair() == RankedHand('Two Pair', 5, [0, 1, 2, 3])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '2'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.two_pair() == None

    def test_one_pair(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '5'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.one_pair() == RankedHand('One Pair', 5, [2, 3])

        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '8'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.one_pair() == None

    def test_high_card(self):
        # Create a hand
        cards = [Card('C', '2'), Card('C', '3'), Card('C', '8'), Card('C', '5'), Card('C', '6')]
        hand = Hand(cards)
        assert hand.high_card() == RankedHand('High Card', 8, [2])

        cards = [Card('C', '2'), Card('C', '3'), Card('C', '8'), Card('C', '5'), Card('C', 'A')]
        hand = Hand(cards)
        assert hand.high_card() == RankedHand('High Card', 14, [4])

    def test_hand_from_string(self):
        hand_string = "5H 5C 6S 7S KD"
        hand = Hand.from_string(hand_string)
        assert hand.cards == [Card('H', '5'), Card('C', '5'), Card('S', '6'), Card('S', '7'), Card('D', 'K')]

    def test_is_flush(self):
        # Create the hand
        hand = Hand.from_string("3D 6D 7D TD QD")

        # Assert it is a flush
        assert hand.flush() is not None

    @pytest.mark.parametrize("id, hand_1, hand_2, left_wins",
                                [
                                    ("1", "5H 5C 6S 7S KD", "2C 3S 8S 8D TD", False), # Hand 1
                                    ("2","5D 8C 9S JS AC", "2C 5C 7D 8S QH", True), # Hand 2
                                    ("3","2D 9C AS AH AC", "3D 6D 7D TD QD", False), # Hand 3
                                    ("4","4D 6S 9H QH QC", "3D 6D 7H QD QS", True), # Hand 4
                                    ("5","2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D", True), # Hand 5
                                    ("5mod","2H 2D 4C 4D 4S", "4C 4D 4S 9S 9D", False), # Hand 5 - same three of a kind
                                ])
    def test_winning_hand(self, id, hand_1, hand_2, left_wins):
        # Create the left hand
        left_hand = Hand.from_string(hand_1)

        # Create the right hand
        right_hand = Hand.from_string(hand_2)

        # Check if the left hand wins
        assert (left_hand > right_hand) == left_wins

        # When reversed, the opposite should be true
        assert (right_hand > left_hand) == (not left_wins)