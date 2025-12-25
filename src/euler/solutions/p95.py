import networkx as nx

from euler import find_factors


def sum_proper_divisors(n):
    # Sum the proper divisors of n
    factors = find_factors(n)
    return sum(factors) - n


# Se can make use of subgraphs/cycles - if we start at a number and get all connected nodes, we are guaranteed to find a repeating cycle
def setup_graph(limit):
    # Setup networkx graph
    G = nx.Graph()

    # Add nodes
    for i in range(1, limit + 1):
        G.add_node(i)

    # Now repeat and connect a number to it's sum of proper divisors IF less than 10**6
    for i in range(1, limit + 1):
        spd = sum_proper_divisors(i)
        if spd <= limit:
            G.add_edge(i, spd)

    return G


def find_longest_cycle(G):
    cycles = nx.cycle_basis(G)

    # Sort by length
    cycles.sort(key=len, reverse=True)

    return cycles[0]


def solution() -> int:
    assert sum_proper_divisors(220) == 284
    assert sum_proper_divisors(284) == 220
    assert sum_proper_divisors(1) == 0
    assert sum_proper_divisors(2) == 1
    assert sum_proper_divisors(3) == 1
    assert sum_proper_divisors(4) == 3

    limit = 10**6
    G = setup_graph(limit)

    longest_cycle = find_longest_cycle(G)
    return min(longest_cycle)


if __name__ == "__main__":
    print(solution())
