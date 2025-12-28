from math import comb


def solution() -> int:
    grid_size = 20
    return comb(2 * grid_size, grid_size)


if __name__ == "__main__":
    print(solution())
