"""
Segment Tree — Point Update, Range Query
─────────────────────────────────────────
Use:   Range sum/min/max queries with point updates
Time:  O(log n) per query and update
Space: O(n)

Change `op` and `identity` to switch between sum / min / max.
"""


class SegTree:
    def __init__(self, data, op=lambda a, b: a + b, identity=0):
        self.n = len(data)
        self.op = op
        self.e = identity
        self.tree = [identity] * (2 * self.n)
        # build
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        """Set position i to val."""
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        """Query op over [l, r) — half-open interval."""
        res = self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.op(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.op(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


# ── Usage ──
# Sum queries:
#   st = SegTree([1, 2, 3, 4, 5])
#   st.query(0, 3)    -> 6  (sum of indices 0,1,2)
#   st.update(1, 10)
#   st.query(0, 3)    -> 14
#
# Min queries:
#   st = SegTree(data, op=min, identity=float('inf'))
#
# Max queries:
#   st = SegTree(data, op=max, identity=float('-inf'))
