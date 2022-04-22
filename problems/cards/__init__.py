from collections import Counter

# Dict of card single letter to value
rank_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
rank_to_name = {'2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', 'T': 'Ten', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}

# Class to hold information about a single card from a pack of cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return rank_to_value[self.rank]

    def __eq__(self, other):
        # Check if two cards are equal
        return self.suit == other.suit and self.rank == other.rank

    def __repr__(self):
        return 'Card(suit=\'' + self.suit + '\', rank=\'' + self.rank + '\')'

    def __str__(self):
        # Display the card as a string (with the suit and rank)
        # Turn rank into a string

        if self.suit == 'C':
            return rank_to_name[self.rank] + ' of Clubs'
        elif self.suit == 'D':
            return rank_to_name[self.rank] + ' of Diamonds'
        elif self.suit == 'H':
            return rank_to_name[self.rank] + ' of Hearts'
        elif self.suit == 'S':
            return rank_to_name[self.rank] + ' of Spades'

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# Class to hold a ranked hand (you can have multiple ranked hands, like Pair of 5s and Pair of 6s) - so this class is expected to be stored in a list
class RankedHand:
    def __init__(self, name, value, indexes):
        self.name = name
        self.value = value
        self.indexes = indexes

    def __eq__(self, other):
        # Check if the two ranked hands are equal
        if self.name == other.name and self.value == other.value and self.indexes == other.indexes:
            return True
        return False

# Class to hold a hand (5 cards)
class Hand:
    def __init__(self, cards):
        self.cards = cards

    def royal_flush(self):
        # Royal flush is a flush and a straight, with an ace
        # Check if flush
        if self.flush():
            # Check if straight
            if self.straight():
                # Check if ace is present
                if 14 in [card.value() for card in self.cards]:
                    return RankedHand('Royal Flush', 14, [0,1,2,3,4])
        return None

    def hand_values(self):
        # Return a list of the values of the cards in the hand
        return [card.value() for card in self.cards]

    def max_hand_value(self):
        # Return the highest value in the hand
        return max(self.hand_values())

    def straight_flush(self):
        # Straight flush is a flush and a straight
        # Check if flush
        if self.flush():
            # Check if straight
            if self.straight():
                return RankedHand('Straight Flush', self.max_hand_value(), [0,1,2,3,4])
        return None

    def four_of_a_kind(self):
        # Four of a kind is four cards of the same value
        # Check if there are four cards of the same value
        value_counts = Counter(self.hand_values())

        for value, count in value_counts.items():
            if count == 4:
                # Get the indexes of the four cards
                indexes = [i for i, card in enumerate(self.cards) if card.value() == value]
                return RankedHand('Four of a Kind', value, indexes)

        return None

    def three_of_a_kind(self):
        # Three of a kind is three cards of the same value
        # Check if there are thtree cards of the same value
        value_counts = Counter(self.hand_values())

        for value, count in value_counts.items():
            if count == 3:
                # Get the indexes of the four cards
                indexes = [i for i, card in enumerate(self.cards) if card.value() == value]
                return RankedHand('Three of a Kind', value, indexes)

        return None

    def flush(self):
        # Flush is all cards of the same suit
        # Check if all cards have the same suit
        if len(set([card.suit for card in self.cards])) == 1:
            return RankedHand('Flush', self.max_hand_value(), [0,1,2,3,4])
        return None

    def straight(self):
        # Straight is all cards in sequence
        # Check if all cards are consecutive values
        if len(set(self.hand_values())) == 5:
            if max(self.hand_values()) - min(self.hand_values()) == 4:
                return RankedHand('Straight', self.max_hand_value(), [0,1,2,3,4])
        return None

    def full_house(self):
        # Full house is three of a kind and a pair
        # Check if there are three cards of the same value
        value_counts = Counter(self.hand_values())

        full_house_potential_value = None
        for value, count in value_counts.items():
            if count == 3:
                # Yes...there is three of a kind, if there is ALSO a pair, then we have a full house
                full_house_potential_value = value

        if full_house_potential_value is not None:
            # Check if there is a pair
            for value, count in value_counts.items():
                if count == 2:
                    # Get the indexes of the three cards
                    indexes = [i for i, card in enumerate(self.cards) if card.value() == full_house_potential_value]
                    return RankedHand('Full House', full_house_potential_value, indexes)

        return None

    def two_pair(self):
        # Two pair is two different pairs
        # Check if there are two pairs
        value_counts = Counter(self.hand_values())

        pair_potential_values = []
        for value, count in value_counts.items():
            if count == 2:
                pair_potential_values.append(value)

        if len(pair_potential_values) == 2:
            # Get the indexes of the four cards
            indexes = [i for i, card in enumerate(self.cards) if card.value() in pair_potential_values]
            return RankedHand('Two Pair', max(pair_potential_values), indexes)

        return None

    def one_pair(self):
        # One pair is two cards of the same value
        # Check if there are two cards of the same value
        value_counts = Counter(self.hand_values())

        pair_potential_values = []
        for value, count in value_counts.items():
            if count == 2:
                pair_potential_values.append(value)

        if len(pair_potential_values) == 1:
            # Get the indexes of the 2 cards
            indexes = [i for i, card in enumerate(self.cards) if card.value() in pair_potential_values]
            return RankedHand('One Pair', max(pair_potential_values), indexes)

        return None

    def high_card(self, ignore_indexes=None):
        # Highest card is the highest value card
        if ignore_indexes is None:
            ignore_indexes = []
        max_value = max([card.value() for i, card in enumerate(self.cards) if i not in ignore_indexes])

        return RankedHand('High Card', max_value, [i for i, card in enumerate(self.cards) if card.value() == max_value][0:1])

    @staticmethod
    def from_string(str_hand):
        # Create a hand from a string of cards
        # Expected format: '2H 3D 5S 9C KD'
        # Return a hand object
        cards = []
        for card_str in str_hand.split(' '):
            cards.append(Card(card_str[1], card_str[0]))
        return Hand(cards)

    def __gt__(self, other):
        # Does this hand beat the other hand?
        # Return True if this hand beats the other hand, False otherwise
        # Royal flush beats all other hands (and we've been told that there is a clear winner)
        if self.royal_flush() is not None:
            return True

        # Straight flush beats four of a kind, full house, flush, straight, three of a kind, two pair, one pair, high card
        if self.straight_flush() is not None:
            if other.straight_flush() is not None:
                return self.straight_flush().value > other.straight_flush().value
            else:
                return True
        else:
            if other.straight_flush() is not None:
                return False

        # Four of a kind beats full house, flush, straight, three of a kind, two pair, one pair, high card
        if self.four_of_a_kind() is not None:
            if other.four_of_a_kind() is not None:
                # Both have four of a kind, compare the values
                if self.four_of_a_kind().value > other.four_of_a_kind().value:
                    return True
                elif self.four_of_a_kind().value == other.four_of_a_kind().value:
                    # Both have four of a kind of the same value, so compare the highest card (but not the four of a kind)
                    return self.high_card(ignore_indexes=self.four_of_a_kind().indexes).value > other.high_card(ignore_indexes=other.four_of_a_kind().indexes).value
                else:
                    return False
            else:
                return True
        else:
            if other.four_of_a_kind() is not None:
                return False

        # Full house beats flush, straight, three of a kind, two pair, one pair, high card
        if self.full_house() is not None:
            if other.full_house() is not None:
                # Both have full house, compare the values
                if self.full_house().value > other.full_house().value:
                    return True
                elif self.full_house().value == other.full_house().value:
                    # Both have full house of the same value, so need to compare the pair value
                    # We can do this by looking at the highest cards without the indexes of the 3 of a kind (we've been told that there will be a clear winner - CAREFUL if that changes!)
                    return self.high_card(ignore_indexes=self.full_house().indexes).value > other.high_card(ignore_indexes=other.full_house().indexes).value
                else:
                    return False
            else:
                return True
        else:
            if other.full_house() is not None:
                return False

        # Flush beats straight, three of a kind, two pair, one pair, high card
        if self.flush() is not None:
            if other.flush() is not None:
                # Both have flush, compare the values (no need to check for highest card, as we've already checked for flush)
                return self.flush().value > other.flush().value
            else:
                return True
        else:
            if other.flush() is not None:
                return False

        # Straight beats three of a kind, two pair, one pair, high card
        if self.straight() is not None:
            if other.straight() is not None:
                # Both have straight, compare the values
                return self.straight().value > other.straight().value
            else:
                return True
        else:
            if other.straight() is not None:
                return False

        # Three of a kind beats two pair, one pair, high card
        if self.three_of_a_kind() is not None:
            if other.three_of_a_kind() is not None:
                # Both have three of a kind, compare the values
                if self.three_of_a_kind().value > other.three_of_a_kind().value:
                    return True
                elif self.three_of_a_kind().value == other.three_of_a_kind().value:
                    # Both have three of a kind of the same value, so compare the highest card (but not the three of a kind)
                    return self.high_card(ignore_indexes=self.three_of_a_kind().indexes).value > other.high_card(ignore_indexes=other.three_of_a_kind().indexes).value
                else:
                    return False
            else:
                return True
        else:
            if other.three_of_a_kind() is not None:
                return False

        # Two pair beats one pair, high card
        if self.two_pair() is not None:
            if other.two_pair() is not None:
                # Both have two pair, compare the values
                if self.two_pair().value > other.two_pair().value:
                    return True
                elif self.two_pair().value == other.two_pair().value:
                    # Both have two pair of the same value, so compare the highest card (but not the two pair)
                    return self.high_card(ignore_indexes=self.two_pair().indexes).value > other.high_card(ignore_indexes=other.two_pair().indexes).value
                else:
                    return False
            else:
                return True
        else:
            if other.two_pair() is not None:
                return False

        # One pair beats high card
        if self.one_pair() is not None:
            if other.one_pair() is not None:
                # Both have one pair, compare the values
                if self.one_pair().value > other.one_pair().value:
                    return True
                elif self.one_pair().value == other.one_pair().value:
                    # Both have one pair of the same value, so compare the highest card (but not the one pair)
                    return self.high_card(ignore_indexes=self.one_pair().indexes).value > other.high_card(ignore_indexes=other.one_pair().indexes).value
                else:
                    return False
            else:
                return True
        else:
            if other.one_pair() is not None:
                return False

        # High card beats nothing
        return self.high_card().value > other.high_card().value
