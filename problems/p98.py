# Print out all the 4 digit numbers that are square
import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import is_square

# Read in the data
with open("data/p98.txt", "r") as f:
    words = f.read().replace('"', '').split(",")

# Create a lookup of set(letters): [words] that can be made with
anagram_options = {}
longest_word = 0
longest_word_set = None

most_anagram_count = 0
most_anagram_set = None

longest_anagram_length = 0
longest_anagram_set = None
for word in words:
    letters = "".join(sorted(word))
    anagram_options.setdefault(letters, []).append(word)
    if len(word) > longest_word:
        longest_word = len(word)
        longest_word_set = letters

    if len(anagram_options[letters]) > most_anagram_count:
        most_anagram_count = len(anagram_options[letters])
        most_anagram_set = letters

    if len(anagram_options[letters]) > 1 and len(word) > longest_anagram_length:
        longest_anagram_length = len(word)
        longest_anagram_set = letters

print(f"Longest word length: {longest_word}")
print(anagram_options[longest_word_set])

print(f"Longest anagram length: {longest_anagram_length}")
print(anagram_options[longest_anagram_set])

# Show a few example that do not have any anagrams
print("Examples of words without anagrams:")
count = 0
for letters, word_options in anagram_options.items():
    if len(word_options) > 1:
        continue

    count += 1
    print(letters, word_options)

    if count > 5:
        break

print(f"Letter set with the most anagrams ({most_anagram_count}):")
print(anagram_options[most_anagram_set])

def apply_lookup(word, lookup):
    new_word = "".join(map(lookup.get, word))
    # Leading 0s are not permitted
    if new_word[0] == '0':
        return 3
    return int(new_word)

def largest_square(set_words):
    # All words in the set will be the same length, they'll also be made up of the same letters
    word = set_words[0]
    # print("Word 1:", word)
    num_unique_letters = len(set(word))
    # print(f"Number unique letters: {num_unique_letters}")

    # Find largest square that is a pair match
    sq_root_max = int((10 ** (len(word)) - 1) ** 0.5) # ie 9999 is 4 chars long, so 99
    sq_root_min = int((10 ** (len(word) - 1)) ** 0.5) # ie 1000 is 4 chars long, so 31

    for sq_root in range(sq_root_max, sq_root_min, -1):
        sq_num = sq_root ** 2
        if not len(set(str(sq_num))) == num_unique_letters:
            continue

        lookup = {c: n for c, n in zip(word, str(sq_num))}

        # See how many of the words form a square when this lookup is applied
        results = [apply_lookup(word, lookup) for word in set_words if is_square(apply_lookup(word, lookup))]
        if len(results) > 1:
            return max(results), lookup

    return None, None

# print("Largest square for CARE and RACE:")
# print(largest_square(["CARE", "RACE"]))

print("Largest square for CREATION and REACTION:")
print(largest_square(["CREATION", "REACTION"]))

# Create lookup of n digits: letter sets
digit_count_lookup = {}
for letters, word_options in anagram_options.items():
    if len(word_options) > 1:
        digit_count_lookup.setdefault(len(word_options[0]), []).append(word_options)

# Show options
print("Solving...")
for letter_count in sorted(digit_count_lookup.keys(), reverse=True):
    print(f"Letter count: {letter_count}. There are {len(digit_count_lookup[letter_count])} different anagrams groups to check")
    print("Example:")
    print(digit_count_lookup[letter_count][0])

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