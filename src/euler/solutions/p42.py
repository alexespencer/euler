from euler import is_triangular


def word_score(word: str) -> int:
    return sum(ord(c) - ord("A") + 1 for c in word)


def solution() -> int:
    with open("data/p42.txt") as f:
        words = f.readline().replace('"', "").strip().split(",")

    return sum(1 for word in words if is_triangular(word_score(word)))


if __name__ == "__main__":
    print(solution())
