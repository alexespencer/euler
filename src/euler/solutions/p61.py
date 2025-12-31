import networkx as nx

from euler import (
    heptagon_n,
    hexagon_n,
    octagon_n,
    pentagon_n,
    square_n,
    triangle_n,
)


def is_cyclic(number1, number2):
    # Convert to strings
    number1 = str(number1)
    number2 = str(number2)

    # Check if the last 2 digits of number1 = the first 2 digits of number2
    return number1[-2:] == number2[:2]


# Go through all nodes and find simple paths (ones without repeated nodes) - if a path has length 6, then we may have a solution
def solution() -> int:
    # Store for the 4 digit numbers (triangle, square, pentagon, hexagon, hepagon, octagon)
    numbers = {}

    for function_i, f in enumerate(
        [triangle_n, square_n, pentagon_n, hexagon_n, heptagon_n, octagon_n]
    ):
        # Find all 4 digit numbers
        i = 1
        while True:
            n = f(i)
            if len(str(n)) == 4:
                numbers.setdefault(function_i + 3, []).append(n)

            if len(str(n)) > 4:
                break
            i += 1

    # Nodes are identified by their type and their number. IE (3, 1035) is a triangle number with the number 1035
    # If we link (directionally) nodes to next node type IF they form a chain, then we should just have to look for a chain of length 6 for the answer (where the end is cyclic to the start)

    # Create a directed graph
    G = nx.DiGraph()

    # Go through each node type and add all the nodes to the graph
    for node_type in numbers.keys():
        # Go through each number
        for number in numbers[node_type]:
            # Create a node
            G.add_node((node_type, number))

    assert is_cyclic(8128, 2882)

    # Repeat, and look for cyclic numbers
    # Go through each node type
    for node_type1 in numbers.keys():
        for node_type2 in numbers.keys():
            if node_type1 == node_type2:
                continue

            # Go through each number
            for number1 in numbers[node_type1]:
                # Go through each number of the next node type
                for number2 in numbers[node_type2]:
                    if is_cyclic(number1, number2):
                        # Link them
                        G.add_edge((node_type1, number1), (node_type2, number2))

    for node in G.nodes():
        # Find a simple path from this node to (0, y) (y can be different but must be cyclic so (y, x) is cyclic)))
        # print("node:", node)
        potential_end_nodes = [
            end_node
            for end_node in G.nodes()
            if end_node != node and is_cyclic(end_node[1], node[1])
        ]
        if potential_end_nodes:
            # print("Finding route to end nodes:", potential_end_nodes)
            for path in nx.all_simple_paths(
                G, source=node, target=potential_end_nodes, cutoff=6
            ):
                # Number of node types in the path (the first element of the node ID)
                number_node_types = len(set([node[0] for node in path]))
                if len(path) == 6 and number_node_types == 6:
                    # Break out of all loops and return the solution
                    return sum([node[1] for node in path])

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solution())
