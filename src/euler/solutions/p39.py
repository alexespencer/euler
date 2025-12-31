from collections import defaultdict

from euler import generate_pythag_triples


def solution() -> int:
    all_triples = generate_pythag_triples(1000)

    perimeter_count = defaultdict(int)
    for triples in all_triples.values():
        for triple in triples:
            perimeter_count[sum(triple)] += 1

    return max(perimeter_count, key=lambda k: perimeter_count[k])


if __name__ == "__main__":
    print(solution())
