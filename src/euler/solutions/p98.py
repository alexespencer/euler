# Print out all the 4 digit numbers that are square
from euler import is_square


def apply_lookup(word, lookup):
    """Apply the digit lookup to the word and return the new word as an int. Return None if the word starts with 0"""
    new_word = "".join(map(lookup.get, word))
    # Leading 0s are not permitted
    if new_word[0] == "0":
        return None

    return int(new_word)


def largest_square(set_words):
    """Finds the largest square that can be formed from the set of words, applying the rules of the problem"""
    # All words in the set will be the same length, they'll also be made up of the same letters
    seed_word = set_words[0]

    num_unique_letters = len(set(seed_word))

    # Find largest square that is a pair match
    sq_root_max = int(
        (10 ** (len(seed_word)) - 1) ** 0.5
    )  # ie 9999 is 4 chars long, so 99
    sq_root_min = int(
        (10 ** (len(seed_word) - 1)) ** 0.5
    )  # ie 1000 is 4 chars long, so 31

    for sq_root in range(sq_root_max, sq_root_min, -1):
        sq_num = sq_root**2
        if not len(set(str(sq_num))) == num_unique_letters:
            continue

        lookup = {c: n for c, n in zip(seed_word, str(sq_num))}

        # See how many of the words form a square when this lookup is applied
        results = []
        for word in set_words:
            new_word_int = apply_lookup(word, lookup)
            if new_word_int and is_square(new_word_int):
                results.append(new_word_int)

        if len(results) > 1:
            return max(results), lookup

    return None, None


def solution() -> int:
    # Read in the data
    with open("data/p98.txt", "r") as f:
        words = f.read().replace('"', "").split(",")

    # Create a lookup of set(letters): [words] that can be made with
    anagram_options = {}

    for word in words:
        letters = "".join(sorted(word))
        anagram_options.setdefault(letters, []).append(word)

    # Create lookup of n digits: letter sets
    digit_count_lookup = {}
    for letters, word_options in anagram_options.items():
        if len(word_options) > 1:
            digit_count_lookup.setdefault(len(word_options[0]), []).append(word_options)

    # Show options
    for letter_count in sorted(digit_count_lookup.keys(), reverse=True):
        digit_largest_square = 0
        for word_set in digit_count_lookup[letter_count]:
            ls, lookup = largest_square(word_set)
            if ls and ls > digit_largest_square:
                digit_largest_square = ls

        if digit_largest_square > 0:
            return digit_largest_square

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solution())
