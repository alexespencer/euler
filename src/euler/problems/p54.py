from euler.cards import canonical


def solution() -> int:
    # Read the poker.txt file into a list of strings
    with open("data/p54_poker.txt") as f:
        lines = f.readlines()
    # Split the lines up by taking the first 5 elements and the last 5 elements
    hands = [
        (" ".join(line.split()[:5]), " ".join(line.split()[-5:])) for line in lines
    ]

    # Go through, create hands and see which hand wins, count how many left hand wins
    count = 0
    for left_hand, right_hand in hands:
        left_hand = canonical(left_hand.split())
        right_hand = canonical(right_hand.split())
        if left_hand > right_hand:
            count += 1

    return count


if __name__ == "__main__":
    print(solution())
