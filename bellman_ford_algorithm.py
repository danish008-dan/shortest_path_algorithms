"""
Bellman-Ford Algorithm
----------------------
Finds shortest paths and detects negative weight cycles.
"""

def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle detection
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative weight cycle detected")
            return None

    return dist


vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('B', 'C', -2),
    ('C', 'D', 2),
    ('A', 'D', 7)
]

print(bellman_ford(vertices, edges, 'A'))
