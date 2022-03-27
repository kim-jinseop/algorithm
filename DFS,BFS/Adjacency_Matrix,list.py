INF = 987654321

# Adjacency Matrix
graph_M = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# Adjacency List
graph_L = [[] for _ in range(3)]

graph_L[0].append((1,7))
graph_L[0].append((2,5))

graph_L[1].append((0,7))

graph_L[2].append((0,5))



print(graph_M)
print(graph_L)