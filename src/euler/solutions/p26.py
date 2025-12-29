from euler import decimal_repeat_cycle_length


def solution() -> int:
    lengths = {d: decimal_repeat_cycle_length(1, d) for d in range(10, 1000)}
    return max(lengths, key=lambda k: lengths[k])


if __name__ == "__main__":
    print(solution())
