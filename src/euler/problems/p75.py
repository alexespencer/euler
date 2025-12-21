from euler import generate_pythag_triples

# For a right angled triangle with integer sides there are a number of properties we might be able to use:
# ((a * b) / 2) % 6 == 9
# a * b * c % 60 == 0
# Or...we can use Euclid's formula, but with the k parameter modification so that ALL triples are generated
# ...where m, n, k are positive integers, and m > n and m,n are coprime (HCF(m,n) == 1) and both not odd


def solution() -> int:
    max_length = 1500000
    triangles = generate_pythag_triples(max_length)

    # How many with only one triangle up to the max_length
    answer = len([1 for L, t in triangles.items() if len(t) == 1 and L <= max_length])
    return answer


if __name__ == "__main__":
    print(solution())
