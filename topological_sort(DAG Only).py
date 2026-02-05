"""
Topological Sort
----------------
Applies to Directed Acyclic Graph (DAG).
"""

from collections import deque

def topological_sort(vertices, edges):
    graph = {v: [] for v in vertices}
    indegree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([v for v in vertices if indegree[v] == 0])
    topo = []

    while queue:
        node = queue.popleft()
        topo.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo


vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]

print(topological_sort(vertices, edges))
