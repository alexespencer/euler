# Problem 84 - monopoly square odds
import random


class Board:
    squares = [
        "GO",
        "A1",
        "CC1",
        "A2",
        "T1",
        "R1",
        "B1",
        "CH1",
        "B2",
        "B3",
        "JAIL",
        "C1",
        "U1",
        "C2",
        "C3",
        "R2",
        "D1",
        "CC2",
        "D2",
        "D3",
        "FP",
        "E1",
        "CH2",
        "E2",
        "E3",
        "R3",
        "F1",
        "F2",
        "U2",
        "F3",
        "G2J",
        "G1",
        "G2",
        "CC3",
        "G3",
        "R4",
        "CH3",
        "H1",
        "T2",
        "H2",
    ]

    def __init__(self, dice_sides):
        self.dice_sides = dice_sides
        self.current_square = 0
        self.square_counts = {s: 0 for s in Board.squares}
        self.dice_rolls = 0
        self.double_rolls = 0

        # Shuffle CC and CH - store in self
        self.CC_choices = ["GO", "JAIL"] + [None] * 14
        self.CC_index = 0
        self.CH_choices = [
            "GO",
            "JAIL",
            "C1",
            "E3",
            "H2",
            "R1",
            "Rx",
            "Rx",
            "Ux",
            "-3",
        ] + [None] * 6
        self.CH_index = 0
        random.shuffle(self.CC_choices)
        random.shuffle(self.CH_choices)

        # For speed, calculate the indexes of R[x] and U[x]
        self.R_indexes = [
            i for i, square in enumerate(Board.squares) if square.startswith("R")
        ]
        self.U_indexes = [
            i for i, square in enumerate(Board.squares) if square.startswith("U")
        ]

    def top_3_squares(self):
        return [
            (x, self.square_counts[x] / self.dice_rolls, Board.squares.index(x))
            for x in sorted(
                self.square_counts, key=lambda x: self.square_counts[x], reverse=True
            )[:3]
        ]

    def dice_score(self):
        # Dice_sides = [6, 6] <--- means you can have any number of dice, with any number of sides
        # Returns the sum and whether at least 1 double is rolled
        rolls = [random.randint(1, side_max) for side_max in self.dice_sides]
        return sum(rolls), len(set(rolls)) < len(rolls)

    def get_CC(self):
        # Get the next CC choice
        self.CC_index += 1
        return self.CC_choices[self.CC_index % len(self.CC_choices)]

    def get_CH(self):
        # Get the next CH choice
        self.CH_index += 1
        return self.CH_choices[self.CH_index % len(self.CH_choices)]

    def get_destination_index(self, action):
        if action == "Rx":
            return min(
                [x for x in self.R_indexes if x > self.current_square],
                default=min(self.R_indexes),
            )
        elif action == "Ux":
            return min(
                [x for x in self.U_indexes if x > self.current_square],
                default=min(self.U_indexes),
            )
        else:
            # Simply return the index of the square
            return Board.squares.index(action)

    def advance_to_square(self, square):
        # Advance to a square and take the action
        self.current_square = square
        self.square_counts[Board.squares[square]] += 1

        return None

    def roll_dice(self):
        # Rolls the dice and take the action(s) and keeps count of where we land
        self.dice_rolls += 1

        # Roll the dice
        dice_score, at_least_1_double = self.dice_score()
        if at_least_1_double:
            self.double_rolls += 1
            if self.double_rolls >= 3:
                self.double_rolls = 0
                return self.advance_to_square(Board.squares.index("JAIL"))
        else:
            self.double_rolls = 0

        # Get next square (might not be the final destination)
        next_square = (self.current_square + dice_score) % len(Board.squares)

        if Board.squares[next_square] == "G2J":
            return self.advance_to_square(Board.squares.index("JAIL"))

        card_action = None
        destination_index = next_square

        # If CC/CH - find the card
        if Board.squares[next_square] in ["CC1", "CC2", "CC3"]:
            card_action = self.get_CC()
        elif Board.squares[next_square] in ["CH1", "CH2", "CH3"]:
            card_action = self.get_CH()

        # Turn the card action into a destination index
        if card_action == "-3":
            destination_index = next_square - 3 % len(Board.squares)
        elif card_action is not None:
            destination_index = self.get_destination_index(card_action)

        # Move the the destination square
        return self.advance_to_square(destination_index)


def solution() -> int:
    random.seed(42)
    b = Board([4, 4])
    for _ in range(1000000):
        b.roll_dice()
    return int("".join(str(x) for _, _, x in b.top_3_squares()))


if __name__ == "__main__":
    print(solution())
