"""
Kruskal's Algorithm
-------------------
Finds Minimum Spanning Tree using Disjoint Set Union (DSU).
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px
            return True
        return False


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst_cost = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst_cost += w

    return mst_cost


edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("MST Cost:", kruskal(4, edges))
