"""
Prim's Algorithm
----------------
Finds Minimum Spanning Tree using greedy approach.
"""

import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))

    return total_cost


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1)],
    'C': [('A', 3), ('B', 1)]
}

print("MST Cost:", prims(graph, 'A'))
