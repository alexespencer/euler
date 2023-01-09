# Roman numerals
import sys, os, time
sys.path.insert(0, os.getcwd())

from roman import number_to_minimal_roman, roman_to_int

# Open the file and read in all lines
with open("data/p89.txt", "r") as f:
    roman_lines = f.readlines()
    roman_lines = [line.strip().replace('\n', '') for line in roman_lines]

# Get total original length
original_length = sum([len(line) for line in roman_lines])

# For each numeral, convert to minimal roman and get the number of characters
roman_minimals = []
for roman in roman_lines:
    num = roman_to_int(roman)
    min_roman = number_to_minimal_roman(num)
    roman_minimals.append((roman, num, min_roman))

    if len(roman) != len(min_roman):
        print(f"{roman} -> {min_roman}")

    if len(min_roman) > len(roman):
        print(f"ERROR: {roman} ({num}) -> {min_roman}")
        exit()

print(roman_minimals[0:5])

# Get total minimal length
minimal_length = sum([len(line[2]) for line in roman_minimals])

print(f"Original length: {original_length}")
print(f"Minimal length: {minimal_length}")
print(f"Saved {original_length - minimal_length} characters")