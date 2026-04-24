"""
Disjoint Set Union (Union-Find)
─────────────────────────────────
Use:   Connected components, cycle detection, Kruskal's MST
Time:  Nearly O(1) amortized per operation (inverse Ackermann)
"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  # size of each component
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Returns True if a and b were in different components."""
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def comp_size(self, x):
        return self.size[self.find(x)]


# ── Usage ──
# dsu = DSU(n)
# dsu.union(0, 1)
# dsu.connected(0, 1)  -> True
# dsu.comp_size(0)     -> 2
# dsu.components       -> number of connected components
