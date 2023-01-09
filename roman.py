# Roman numeral functions

roman_numerals = {  "I" : 1,
                    "V" : 5,
                    "IX" : 9,
                    "X" : 10,
                    "L" : 50,
                    "XC" : 90,
                    "C" : 100,
                    "D" : 500,
                    "CM" : 900,
                    "M" : 1000}

# 3 main rules:
# 1) Numerals must be arranged in descending order of size.
# 2) M, C, and X cannot be equalled or exceeded by smaller denominations.
# 3) D, L, and V can each only appear once

# Subtractive rules (for rule 1):
# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M

def split_into_groups(numeral):
    """Splits a numeral into groups bounded by subtractive rules"""
    groups = []
    current_group = []
    for i in range(len(numeral)):
        current_numeral = numeral[i]
        current_num = roman_numerals[current_numeral]

        if not current_group:
            # Current group is empty
            current_group.append(current_numeral)
        else:
            # If the current number is greater than the last number in the group, then we have a subtractive pair
            if current_num > roman_numerals[current_group[-1]]:
                current_group.append(current_numeral)
                groups.append(current_group)
                current_group = []
            else:
                # Otherwise, we have a new group
                groups.append(current_group)
                current_group = [current_numeral]

    if current_group:
        groups.append(current_group)

    return groups

def roman_to_int(numeral):
    """Converts a roman numeral to an int"""
    if not rule_1(numeral):
        raise ValueError("Rule 1 broken")

    if not rule_2(numeral):
        raise ValueError("Rule 2 broken")

    if not rule_3(numeral):
        raise ValueError("Rule 3 broken")

    total = 0
    for i in range(len(numeral)):
        current_num = roman_numerals[numeral[i]]
        next_num = roman_numerals[numeral[i+1]] if i != len(numeral) - 1 else None

        if next_num is None:
            total += current_num
        elif current_num < next_num:
            total -= current_num
        else:
            total += current_num

    return total

def rule_1(numeral):
    "Checks if rule 1 is broken"
    # Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
    # I can only be placed before V and X.
    # X can only be placed before L and C.
    # C can only be placed before D and M
    groups = split_into_groups(numeral)
    for group in groups:
        # If the group has 2 items, the first must be I, X, or C
        if len(group) == 2:
            if group[0] not in ["I", "X", "C"]:
                return False

            # If the first item is I, the second must be V or X
            if group[0] == "I" and group[1] not in ["V", "X"]:
                return False

            # If the first item is X, the second must be L or C
            if group[0] == "X" and group[1] not in ["L", "C"]:
                return False

            # If the first item is C, the second must be D or M
            if group[0] == "C" and group[1] not in ["D", "M"]:
                return False

    # If we get here, then the rules are followed
    return True

def rule_2(numeral):
    """Checks if rule 2 is broken"""
    # M, C, and X cannot be equalled or exceeded by smaller denominations.

    # First, we need to split the numeral into groups
    groups = split_into_groups(numeral)

    # Check for repeating groups
    current_group = None
    current_count = 0
    for group in groups:

        if group[0] == current_group:
            current_count += 1
        else:
            current_group = group[0]
            current_count = 1

        if current_group in ["I", "X", "C"] and current_count >= 10:
            return False

    # Must be OK
    return True

def rule_3(numeral):
    """Checks if rule 3 is broken"""
    for char in ["D", "L", "V"]:
        if numeral.count(char) > 1:
            return False

    return True

def find_subtractive_pair(number):
    """Finds a potential subtractive pair for a number, if there is one"""
    potential_second = None
    for roman, integer in roman_numerals.items():
        if len(roman) > 1:
            continue

        if integer > number:
            potential_second = [roman, integer]
            break

    if potential_second is None:
        return None

    potential_first = None
    for roman, integer in roman_numerals.items():
        if len(roman) > 1:
            continue

        if potential_second[1] - number == integer:
            potential_first = [roman, integer]
            break

    if potential_first is None:
        return None

    potential_numeral = potential_first[0] + potential_second[0]
    if rule_1(potential_numeral):
        return potential_numeral

    return None

def number_to_minimal_roman(num):
    """Converts a number to a minimal roman numeral"""
    remaining = num
    numeral = ""

    # Until remaining is 0, keep going
    while remaining > 0:
        # print(remaining)

        # Potential is either n x the largest number that is less than or equal to remaining,
        # or it is a subtractive pair of EITHER the remaining number, or a SP of the biggest possible chunk
        # Whichever is shorter

        biggest_possible = [(roman, integer) for roman, integer in roman_numerals.items() if integer <= remaining][-1]
        count = remaining // biggest_possible[1]
        deduct = count * biggest_possible[1]
        # print(f"Either straight to {remaining}, or deducting {deduct}, using {count} of {biggest_possible[0]}")

        # Either its a subtractive pair of the remaining number, or a subtractive pair of the biggest possible chunk
        subtractive_pair_direct = find_subtractive_pair(remaining)
        if subtractive_pair_direct is not None:
            # print(f"Subtractive pair of {remaining} is {subtractive_pair_direct}")
            numeral += subtractive_pair_direct
            remaining -= roman_to_int(subtractive_pair_direct)
            continue

        subtractive_pair_chunk = find_subtractive_pair(deduct)
        if subtractive_pair_chunk is not None and len(subtractive_pair_chunk) < len(biggest_possible[0]) * count:
            # print(f"Subtractive pair of {deduct} is {subtractive_pair_chunk}")
            numeral += subtractive_pair_chunk
            remaining -= roman_to_int(subtractive_pair_chunk)
            continue

        # print(f"Using {count} of {biggest_possible[0]}")
        numeral += biggest_possible[0] * count
        remaining -= deduct
        # print(numeral)

    if not (rule_1(numeral) and rule_2(numeral) and rule_3(numeral)):
        raise ValueError("Rule 1 broken")

    return numeral
