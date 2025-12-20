import networkx as nx

# Rather than write our own algo, this is equivalent to Djikstra's algo, let's use networkx

# Same as 81 but can move up/down/left and right!


def minimal_path(matrix):
    # Setup networkx graph
    G = nx.DiGraph()

    # Add nodes
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            G.add_node((i, j))

    # Now repeat for edges
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            # Up
            if i - 1 >= 0:
                G.add_edge((i, j), (i - 1, j), weight=matrix[i - 1][j])

            # Down
            if i + 1 < len(matrix):
                G.add_edge((i, j), (i + 1, j), weight=matrix[i + 1][j])

            # Left
            if j - 1 >= 0:
                G.add_edge((i, j), (i, j - 1), weight=matrix[i][j - 1])

            # Right
            if j + 1 < len(matrix[i]):
                G.add_edge((i, j), (i, j + 1), weight=matrix[i][j + 1])

    distance, _ = nx.single_source_dijkstra(
        G, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1)
    )

    # Add on the start
    distance += matrix[0][0]

    return distance


matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

assert minimal_path(matrix) == 2297

# Read in the pyramid
matrix = []
with open("data/p81.txt", "r") as f:
    for line in f:
        matrix.append(list(map(int, line.split(","))))

print("Minimum path sum (up, down or right):", minimal_path(matrix))
