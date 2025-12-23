from itertools import permutations

from euler import is_cube


def count_cube_permutations(n):
    """Count the number of permutations of n that are cubes"""
    perms = []
    for permutation in list(set(permutations(str(n)))):
        if permutation[0] == "0":
            continue
        permutation = int("".join(permutation))
        if permutation not in perms and is_cube(permutation):
            perms.append(permutation)

    return len(perms)


def solution() -> int:
    assert count_cube_permutations(41063625) == 3

    # We'll need to store cube numbers and check permutations in a dictionary
    # Or - we go through the cubes (once) and store their ordered digits, and when we've found all X digit cubes look for N number having the same ordered digits

    find_x_perms = 5
    n = 1  # Start at 999 when searching for 5 perms
    number_digits = len(str(n**3))
    number_digits_to_cube_numbers = {}  # Format will be number {digits : {ordered digits : [cube numbers]}}

    while True:
        n += 1
        cube_number = n**3

        # If the number of digits has changed, look through the results and see if we have the required number of perms
        if len(str(cube_number)) != number_digits:
            # Run our check now (if the dictionary has results, that is)
            if number_digits in number_digits_to_cube_numbers:
                # Check if any of the ordered digits have the number of entries required, get the minimum (there may be multiple solutions, non-minimal)
                min_found = min(
                    [
                        min(cube_numbers)
                        for cube_numbers in number_digits_to_cube_numbers[
                            number_digits
                        ].values()
                        if len(cube_numbers) == find_x_perms
                    ],
                    default=None,
                )

                if min_found is not None:
                    return min_found

                # Reset dict
                number_digits_to_cube_numbers = {}

        number_digits = len(str(cube_number))

        # Get the ordered digits of the cube number
        digits = "".join(sorted(str(cube_number)))

        # Add to the dictionary for the number of digits
        number_digits_to_cube_numbers.setdefault(number_digits, {}).setdefault(
            digits, []
        ).append(cube_number)


if __name__ == "__main__":
    print(solution())
