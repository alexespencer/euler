def solution() -> int:
    values = {}
    x = 0
    y = 0
    value = 1

    # Add the 1
    values[(x, y)] = value

    # Add the other layers
    for step in range(3, 1001 + 1, 2):
        # Take a step to the right
        value += 1
        x += 1

        # Down (1 less than step)
        for _ in range(step - 2):
            values[(x, y)] = value
            y += 1
            value += 1
        values[(x, y)] = value

        # Walk left
        for _ in range(step - 1):
            values[(x, y)] = value
            x -= 1
            value += 1

        values[(x, y)] = value

        # Walk up
        for _ in range(step - 1):
            values[(x, y)] = value
            y -= 1
            value += 1

        values[(x, y)] = value

        # Walk right
        for _ in range(step - 1):
            x += 1
            values[(x, y)] = value
            value += 1

        values[(x, y)] = value

    diagonal_sum = 0
    for (x, y), value in values.items():
        if abs(x) == abs(y):
            diagonal_sum += value

    return diagonal_sum


if __name__ == "__main__":
    print(solution())
