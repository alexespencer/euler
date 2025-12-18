# Print out all the 4 digit numbers that are square
import sys
import os
import time

sys.path.insert(0, os.getcwd())

from euler import is_square


# Declare functions
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


start_time = time.time()
last_time = start_time

print("Reading in words...")
# Read in the data
with open("data/p98.txt", "r") as f:
    words = f.read().replace('"', "").split(",")
print(f"Read in {len(words)} words in {time.time() - last_time:.2f} seconds")
last_time = time.time()

# Create a lookup of set(letters): [words] that can be made with
print("Finding anagrams...")
anagram_options = {}

for word in words:
    letters = "".join(sorted(word))
    anagram_options.setdefault(letters, []).append(word)

# Create lookup of n digits: letter sets
digit_count_lookup = {}
for letters, word_options in anagram_options.items():
    if len(word_options) > 1:
        digit_count_lookup.setdefault(len(word_options[0]), []).append(word_options)
print(f"Found {len(anagram_options)} anagrams in {time.time() - last_time:.2f} seconds")
last_time = time.time()

# Show options
print("Solving...")
for letter_count in sorted(digit_count_lookup.keys(), reverse=True):
    print("Checking letter count: ", letter_count)
    digit_largest_square = 0
    lookup_used = None
    word_set_used = None
    for word_set in digit_count_lookup[letter_count]:
        ls, lookup = largest_square(word_set)
        if ls and ls > digit_largest_square:
            digit_largest_square = ls
            lookup_used = lookup
            word_set_used = word_set

    if digit_largest_square > 0:
        print("Found largest square: ", digit_largest_square)
        # Apply the lookup to each
        print("Word results:")
        for word in word_set_used:
            print(word, apply_lookup(word, lookup_used))
        break

print(f"Found largest square in {time.time() - last_time:.2f} seconds")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
