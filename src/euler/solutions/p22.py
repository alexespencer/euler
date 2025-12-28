def name_letter_score(name: str) -> int:
    return sum([ord(c.upper()) - ord("A") + 1 for c in name])


def solution() -> int:
    assert name_letter_score("COLIN") == 53

    with open("data/p22.txt") as f:
        names = f.readline().strip().replace('"', "").split(",")

    # Sort names alphabetically
    names.sort()

    # Return sum of product of location * score
    total_score = 0
    for index, name in enumerate(names):
        total_score += (index + 1) * name_letter_score(name)

    return total_score


if __name__ == "__main__":
    print(solution())
