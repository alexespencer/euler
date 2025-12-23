# 5-gon ring
from itertools import permutations


# Storange for the lists (See if we can create the 3 gon ring solution first)
class GonRing:
    lines: list[list[int | None]]

    map = [
        None,
        [-1, 2],
        [1, 1],
    ]  # When you set node 0, it doesn't affect anything else.

    # When you set node 1, it affects the line before it and the 2nd (by ID) node on that line
    # When you set node 2, it affects the line after it and the middle node (ID 1) on that line
    def __init__(self, default=None):
        self.lines = [[default, default, default] for i in range(5)]

    def set_node(self, line, node, value):
        side_effect = self.map[node]

        self.lines[line][node] = value

        if side_effect:
            other_line = self.lines[(line + side_effect[0]) % 5]
            other_line[side_effect[1]] = value

    def is_magic(self):
        # Is the sum of each line the same?
        lines = [[x for x in line if x is not None] for line in self.lines]
        sums = list(map(sum, lines))
        return len(set(sums)) == 1

    def string_representation(self):
        # Starting with the line with the smallest first node and working clockwise
        # Return a string representation of the 5-gon ring
        # Get the line with the smallest first node
        lines = [[x for x in line if x is not None] for line in self.lines]
        # Find the smallest first node value among the lines (these sublists contain only ints)
        min_first = min(line[0] for line in lines)
        # Locate the index of the line in `self.lines` whose first element equals that minimum.
        # Use `next` with `enumerate` so types remain compatible (self.lines elements can contain None).
        starting_id = next(i for i, L in enumerate(self.lines) if L[0] == min_first)
        str_repr = ""

        for id in range(starting_id, starting_id + 5):
            actual_id = id % 5
            str_repr += "".join(map(str, self.lines[actual_id]))

        return str_repr


def solution() -> int:
    settable = [
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 2],
        [2, 0],
        [2, 2],
        [3, 0],
        [3, 2],
        [4, 0],
    ]

    # Quick test
    gr = GonRing()
    for i in range(1, 11):
        gr.set_node(settable[i - 1][0], settable[i - 1][1], i)
    assert gr.string_representation() == "1234356578791092"

    gr = GonRing()
    for i in range(1, 11):
        gr.set_node(settable[i - 1][0], settable[i - 1][1], i)
    gr.set_node(0, 0, 9)
    assert gr.string_representation() == "4356578791092923"

    # There are 10! = 3,628,800 possible solution ... not too bad
    allowed_numbers = [i for i in range(1, 11)]

    # Try a faster route - this takes 0.25 seconds. If I turned this into a recursive function with more line/perm[-1] checking it would be a lot faster
    max_string_repr_found = 0
    for perm in permutations(allowed_numbers, 3):
        line_sum = sum(perm)

        # Remove the perm from the allowed_numbers
        new_allowed_numbers = [i for i in allowed_numbers if i not in perm]
        for perm2 in permutations(new_allowed_numbers, 2):
            if sum(perm2) + perm[-1] != line_sum:
                continue

            # Set up the GonRing
            gr = GonRing()
            zip_actions = zip(perm + perm2, settable[0:5])
            for value, (line, node) in zip_actions:
                gr.set_node(line, node, value)

            # Get new allowed numbers
            new_allowed_numbers2 = [i for i in new_allowed_numbers if i not in perm2]

            # Determine other nodes in the old way
            for perm3 in permutations(new_allowed_numbers2):
                zip_actions2 = zip(perm3, settable[5:])
                for value, (line, node) in zip_actions2:
                    gr.set_node(line, node, value)

                if gr.is_magic():
                    str_repr = gr.string_representation()
                    if len(str_repr) == 16 and int(str_repr) > max_string_repr_found:
                        max_string_repr_found = int(gr.string_representation())

    return max_string_repr_found


if __name__ == "__main__":
    print(solution())
