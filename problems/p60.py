# I am quite proud of this solution (using cliques within a graph)

import pickle
import sys, os
sys.path.insert(0, os.getcwd())

from euler import is_prime

from itertools import combinations
from functools import reduce

import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(lambda a,b: a*b, range(n, n-r, -1), 1)
    denom = reduce(lambda a,b: a*b, range(1, r+1), 1)
    return numer//denom

# Get primes up to 10000
limit = 10000
primes = [2] + [i for i in range(3, limit, 2) if is_prime(i)]

# How many primes?
print(f"There are {len(primes)} primes")
print(f"Checking {ncr(len(primes), 2)} prime pairs for concatentation")

# Generate pairs that concatenate (in either order) to make a prime
# If pickle file exists, load it
pickle_file = f"data/prime_pairs_{limit}.pickle"
if os.path.exists(pickle_file):
    with open(pickle_file, 'rb') as f:
        prime_pairs = pickle.load(f)
else:
    # Create them now
    prime_pairs = []
    for prime1, prime2 in combinations(primes, 2):
        if is_prime(int(str(prime1) + str(prime2))) and is_prime(int(str(prime2) + str(prime1))):
            prime_pairs.append((prime1, prime2))

    # Pickle the prime pairs for faster restart
    with open(pickle_file, 'wb') as f:
        pickle.dump(prime_pairs, f)

print(f"Prime pairs count: {len(prime_pairs)}")

# Create a graph of connections
G = nx.Graph()
G.add_nodes_from(primes)
G.add_edges_from(prime_pairs)

# Find cliques
potential_cliques = []
for clique in enumerate_all_cliques(G):
    if len(clique) == 5:
        potential_cliques.append(clique)
        print(clique)
        print(sum(clique))

# Print the clique with the minimum sum
if potential_cliques:
    print(f"Minimum clique sum: {min([sum(c) for c in potential_cliques])}")
else:
    print("No cliques found - try increasing the limit")