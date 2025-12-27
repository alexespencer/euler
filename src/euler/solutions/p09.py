from euler import generate_pythag_triples


def solution() -> int:
    length_to_triples = generate_pythag_triples(1000 + 1)
    for triples in length_to_triples.values():
        for a, b, c in triples:
            if a + b + c == 1000:
                return a * b * c
    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solution())
