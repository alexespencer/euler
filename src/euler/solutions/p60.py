# I am quite proud of this solution (using cliques within a graph)

from itertools import combinations

import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques

from euler.primes import is_prime


def solution() -> int:
    # Get primes up to 10000
    limit = 10000
    primes = [2] + [i for i in range(3, limit, 2) if is_prime(i)]

    # Generate pairs that concatenate (in either order) to make a prime
    prime_pairs = []
    for prime1, prime2 in combinations(primes, 2):
        if is_prime(int(str(prime1) + str(prime2))) and is_prime(
            int(str(prime2) + str(prime1))
        ):
            prime_pairs.append((prime1, prime2))

    # Create a graph of connections
    G = nx.Graph()
    G.add_nodes_from(primes)
    G.add_edges_from(prime_pairs)

    # Find cliques
    potential_cliques = []
    for clique in enumerate_all_cliques(G):
        if len(clique) == 5:
            potential_cliques.append(clique)

    # Print the clique with the minimum sum
    if potential_cliques:
        return min([sum(c) for c in potential_cliques])

    raise ValueError("No clique of size 5 found")


if __name__ == "__main__":
    print(solution())
