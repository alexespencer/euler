from euler.roman import number_to_minimal_roman, roman_to_int


def solution() -> int:
    # Open the file and read in all lines
    with open("data/p89.txt", "r") as f:
        roman_lines = f.readlines()
        roman_lines = [line.strip().replace("\n", "") for line in roman_lines]

    # Get total original length
    original_length = sum([len(line) for line in roman_lines])

    # For each numeral, convert to minimal roman and get the number of characters
    roman_minimals = []
    for roman in roman_lines:
        num = roman_to_int(roman)
        min_roman = number_to_minimal_roman(num)
        roman_minimals.append((roman, num, min_roman))

        if len(min_roman) > len(roman):
            raise ValueError("Minimal roman longer than original!")

    # Get total minimal length
    minimal_length = sum([len(line[2]) for line in roman_minimals])

    return original_length - minimal_length


if __name__ == "__main__":
    print(solution())
