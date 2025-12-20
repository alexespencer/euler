from itertools import permutations

# Import the cipher.txt file into a list
with open("data/p59_cipher.txt") as f:
    line = f.readline()

    # Split the line up by comma and convert to integers
    cipher_bytes = [int(x) for x in line.split(",")]

assert cipher_bytes[0:5] == [36, 22, 80, 0, 0]

# The encryption key consists of 3 lowercase characters - but we do not know the length? Assume 3 for now


def encrypt(plain_text, password):
    # Repeat the password so it exactly matches the encrypted bytes length
    password = password * (int(len(plain_text) / len(password)) + 1)
    password = password[0 : len(plain_text)]

    # Convert the plain text to bytes (ascii)
    plain_text = bytes(plain_text, "ascii")

    # Encrypt the bytes
    encrypted_bytes = []
    for i in range(len(plain_text)):
        encrypted_bytes.append(plain_text[i] ^ ord(password[i]))

    return encrypted_bytes


def decrypt(encrypted_bytes, password):
    # Repeat the password so it exactly matches the encrypted bytes length
    password = password * (int(len(encrypted_bytes) / len(password)) + 1)
    password = password[0 : len(encrypted_bytes)]

    # Decrypt the bytes
    decrypted_bytes = []
    for i in range(len(encrypted_bytes)):
        decrypted_bytes.append(encrypted_bytes[i] ^ ord(password[i]))

    # Convert the decrypted bytes to a string
    decrypted_string = "".join(chr(x) for x in decrypted_bytes)
    return decrypted_string


raw_text = "This is a string"
password = "bob"
encrypted_bytes = encrypt(raw_text, password)
decrypted_string = decrypt(encrypted_bytes, password)
# print(encrypted_bytes)
assert raw_text == decrypted_string


def crack_encryption(encrypted_bytes, password_length=3):
    # Run through all the password combinations and look for key words and phrases
    key_phrases = [
        "the",
        "at",
        "there",
        "some",
        "my",
        "of",
        "be",
        "use",
        "her",
        "than",
        "and",
        "this",
        "an",
        "would",
        "first",
        "a",
        "have",
        "each",
        "make",
        "water",
        "to",
        "from",
        "which",
        "like",
        "been",
        "in",
        "or",
        "she",
        "him",
        "call",
        "is",
        "one",
        "do",
        "into",
        "who",
        "you",
        "had",
        "how",
        "time",
        "oil",
        "that",
        "by",
        "their",
        "has",
        "its",
        "it",
        "word",
        "if",
        "look",
        "now",
        "he",
        "but",
        "will",
        "two",
        "find",
        "was",
        "not",
        "up",
        "more",
        "long",
        "for",
        "what",
        "other",
        "write",
        "down",
        "on",
        "all",
        "about",
        "go",
        "day",
        "are",
        "were",
        "out",
        "see",
        "did",
        "as",
        "we",
        "many",
        "number",
        "get",
        "with",
        "when",
        "then",
        "no",
        "come",
        "his",
        "your",
        "them",
        "way",
        "made",
        "they",
        "can",
        "these",
        "could",
        "may",
        "I",
        "said",
        "so",
        "people",
        "part",
    ]

    # Run through all the possible passwords
    allowed_password_chars = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    results = []

    for password in permutations(allowed_password_chars, password_length):
        password = "".join(password)
        decrypted_string = decrypt(encrypted_bytes, password)

        # Check if the decrypted string contains any of the key phrases
        count_key_phrases = 0

        # Get percentage of characters that are a-zA-Z
        count_alpha = sum([c.isalpha() for c in decrypted_string])

        # Count how many of the key phrases are in the decrypted string
        for key_phrase in key_phrases:
            if key_phrase in decrypted_string:
                count_key_phrases += 1

        results.append(
            (
                count_alpha * count_key_phrases,
                count_alpha,
                count_key_phrases,
                password,
                decrypted_string,
            )
        )

    # Sort the results by the score
    results.sort(key=lambda x: x[0], reverse=True)

    print(f"Password length: {password_length}")
    for i in range(2):
        print(results[i])

    return results[0][3]


most_likely_password = crack_encryption(cipher_bytes, 3)

# Find the sum of the ASCII values in the original text using the password found
original_text = decrypt(cipher_bytes, most_likely_password)
original_bytes = bytes(original_text, "ascii")
print(sum(original_bytes))
