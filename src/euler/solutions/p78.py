# Analogous to P76, but with + 1? Maybe - but we need a faster p(n) function. We can use the Euler function of alternating pentagon powers to generate the p(n) function.
from euler import pentagon_n


def get_pentagonal_power(n, pentagon_cache):
    n += 1
    x = int(n / 2)
    if n % 2 == 1:
        x *= -1

    # print(n // 2)

    if x in pentagon_cache:
        return pentagon_cache[x]
    else:
        pentagon_cache[x] = pentagon_n(x) * (-1 if (n // 2) % 2 == 0 else 1)
        return pentagon_cache[x]


def get_action_seq(length, pentagon_cache):
    # This isn't optimal - we are repeatedly accessing the same values - we could grow the action seq too
    i = 1

    while abs(get_pentagonal_power(i, pentagon_cache)) <= length:
        yield get_pentagonal_power(i, pentagon_cache)
        i += 1


def get_next_seq(pentagon_cache, seq):
    # Get the additions/subtractions we will have to make
    actions = list(get_action_seq(len(seq), pentagon_cache))

    pn = 0
    for action in list(actions):
        if action > 0:
            pn += seq[-action]
        else:
            pn -= seq[action]
    seq.append(pn)

    return pn, len(seq) - 1


def solution() -> int:
    pentagon_cache = {}
    seq = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]

    while True:
        pn, n = get_next_seq(pentagon_cache, seq)
        if pn % 10**6 == 0:
            return n


if __name__ == "__main__":
    print(solution())
