"""
Data Structures — DSU, Segment Tree, Fenwick Tree
══════════════════════════════════════════════════
"""


# ── DSU / Union-Find ─────────────────────────
# Use:   Connected components, cycle detection, Kruskal's MST
# Time:  Nearly O(1) amortized per operation

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
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

# dsu = DSU(n)
# dsu.union(0, 1)
# dsu.connected(0, 1)  -> True
# dsu.comp_size(0)      -> 2
# dsu.components        -> number of connected components


# ── Segment Tree (point update, range query) ─
# Use:   Range sum/min/max with point updates
# Time:  O(log n) per query and update
# Swap op/identity for sum vs min vs max

class SegTree:
    def __init__(self, data, op=lambda a, b: a + b, identity=0):
        self.n = len(data)
        self.op = op
        self.e = identity
        self.tree = [identity] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        """Query over [l, r) half-open."""
        res = self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.op(res, self.tree[l]); l += 1
            if r & 1:
                r -= 1; res = self.op(res, self.tree[r])
            l >>= 1; r >>= 1
        return res

# st = SegTree([1,2,3,4,5])          # sum
# st = SegTree(data, min, float('inf'))  # min
# st = SegTree(data, max, float('-inf')) # max
# st.query(0, 3)  -> op over indices 0,1,2
# st.update(1, 10)


# ── Fenwick Tree / BIT ───────────────────────
# Use:   Prefix sums + point updates (lighter than seg tree)
# Time:  O(log n) per operation

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix(self, i):
        """Sum of [0, i] inclusive."""
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query(self, l, r):
        """Sum of [l, r] inclusive."""
        return self.prefix(r) - (self.prefix(l - 1) if l > 0 else 0)

    @classmethod
    def from_array(cls, arr):
        bit = cls(len(arr))
        for i, v in enumerate(arr):
            bit.update(i, v)
        return bit

# bit = BIT(n)
# bit.update(2, 5)       # arr[2] += 5
# bit.query(2, 4)        # sum of arr[2..4]
# bit = BIT.from_array([1, 2, 3, 4, 5])
