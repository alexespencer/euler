from itertools import permutations


def meets_property(str_n: str) -> bool:
    if int(str_n[1 : 1 + 3]) % 2 != 0:
        return False

    if int(str_n[2 : 2 + 3]) % 3 != 0:
        return False

    if int(str_n[3 : 3 + 3]) % 5 != 0:
        return False

    if int(str_n[4 : 4 + 3]) % 7 != 0:
        return False

    if int(str_n[5 : 5 + 3]) % 11 != 0:
        return False

    if int(str_n[6 : 6 + 3]) % 13 != 0:
        return False

    if int(str_n[7 : 7 + 3]) % 17 != 0:
        return False

    return True


def solution() -> int:
    assert meets_property("1406357289") is True

    total = 0
    for perm in permutations(range(10), 10):
        if perm[0] == 0:
            continue
        str_n = "".join(map(str, perm))
        if meets_property(str_n):
            total += int(str_n)

    return total


if __name__ == "__main__":
    print(solution())
