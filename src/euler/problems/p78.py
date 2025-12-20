# Analogous to P76, but with + 1? Maybe - but we need a faster p(n) function. We can use the Euler function of alternating pentagon powers to generate the p(n) function.
import time

from euler import pentagon_n

pentagon = {}


def get_pentagonal_power(n):
    n += 1
    x = int(n / 2)
    if n % 2 == 1:
        x *= -1

    # print(n // 2)

    if x in pentagon:
        return pentagon[x]
    else:
        pentagon[x] = pentagon_n(x) * (-1 if (n // 2) % 2 == 0 else 1)
        return pentagon[x]


seq = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]


def get_action_seq(length):
    # This isn't optimal - we are repeatedly accessing the same values - we could grow the action seq too
    i = 1

    while abs(get_pentagonal_power(i)) <= length:
        yield get_pentagonal_power(i)
        i += 1


def get_next_seq():
    # Get the additions/subtractions we will have to make
    actions = list(get_action_seq(len(seq)))

    pn = 0
    for action in list(actions):
        if action > 0:
            pn += seq[-action]
        else:
            pn -= seq[action]
    seq.append(pn)

    return pn, len(seq) - 1


starttime = time.time()
while True:
    pn, n = get_next_seq()
    if n % 10000 == 0:
        print(n)
    if pn % 10**6 == 0:
        print(
            f"The least value of n for which p(n) is divisible by one million is {n}."
        )
        break
endtime = time.time()
print(f"Time taken: {endtime - starttime}")
