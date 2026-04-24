"""
Fenwick Tree (Binary Indexed Tree)
──────────────────────────────────
Use:   Prefix sum queries + point updates (lighter than seg tree)
Time:  O(log n) per operation
Space: O(n)
"""


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        """Add delta to position i (0-indexed)."""
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix(self, i):
        """Sum of [0, i] inclusive (0-indexed)."""
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query(self, l, r):
        """Sum of [l, r] inclusive (0-indexed)."""
        return self.prefix(r) - (self.prefix(l - 1) if l > 0 else 0)

    @classmethod
    def from_array(cls, arr):
        bit = cls(len(arr))
        for i, v in enumerate(arr):
            bit.update(i, v)
        return bit


# ── Usage ──
# bit = BIT(n)
# bit.update(2, 5)      # arr[2] += 5
# bit.prefix(4)          # sum of arr[0..4]
# bit.query(2, 4)        # sum of arr[2..4]
# bit = BIT.from_array([1, 2, 3, 4, 5])
