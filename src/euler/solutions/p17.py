units = {
    0: {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    },
    1: {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    },
    2: "hundred",
    3: "thousand",
}


def to_word(n: int) -> str:
    # If has thousand, return that (and subtract and recurse)
    if n >= 1000:
        current = units[0][n // 1000] + units[3]
        next = to_word(n % 1000)
        return current + ("and" if next != "" else "") + next

    # If has hundred, return that (and subtract and recurse)
    if n >= 100:
        current = units[0][n // 100] + units[2]
        next = to_word(n % 100)
        return current + ("and" if next != "" else "") + next

    # If has ten, return that (and subtract and recurse)
    if n >= 20:
        current = units[1][n // 10]
        next = to_word(n % 10)
        return current + next

    if n >= 10:
        if n == 10:
            return units[1][1]
        elif n == 11:
            return "eleven"
        elif n == 12:
            return "twelve"
        elif n == 13:
            return "thirteen"
        elif n == 14:
            return "fourteen"
        elif n == 15:
            return "fifteen"
        elif n == 16:
            return "sixteen"
        elif n == 17:
            return "seventeen"
        elif n == 18:
            return "eighteen"
        elif n == 19:
            return "nineteen"

    if n == 0:
        return ""

    # If units, return
    return units[0][n]


def solution() -> int:
    total_chars = 0
    for i in range(1, 1000 + 1):
        word = to_word(i)
        total_chars += len(word)
    return total_chars


if __name__ == "__main__":
    print(solution())
