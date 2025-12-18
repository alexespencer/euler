
import networkx as nx

import sys
import os
import time
sys.path.insert(0, os.getcwd())

from euler import find_factors

def sum_proper_divisors(n):
    # Sum the proper divisors of n
    factors = find_factors(n)
    return sum(factors) - n

assert sum_proper_divisors(220) == 284
assert sum_proper_divisors(284) == 220
assert sum_proper_divisors(1) == 0
assert sum_proper_divisors(2) == 1
assert sum_proper_divisors(3) == 1
assert sum_proper_divisors(4) == 3

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

start_time = time.time()

limit = 10**6
print(f"Setup graph for limit {limit}...")
G = setup_graph(limit)
print(G)

def find_longest_cycle(G):
    cycles = nx.cycle_basis(G)

    # Sort by length
    cycles.sort(key=len, reverse=True)

    return cycles[0]

print("Find longest cycle...")
longest_cycle = find_longest_cycle(G)
end_time = time.time()
print(f"Longest cycle length {len(longest_cycle)}: {longest_cycle}")
print(f"Min of longest cycle: {min(longest_cycle)}")
print(f"Time taken: {(end_time - start_time):.2f} seconds")

# Time taken: 118.46926236152649 seconds