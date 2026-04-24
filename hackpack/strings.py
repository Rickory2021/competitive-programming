"""
Strings — Z-function, KMP, Polynomial Hashing
══════════════════════════════════════════════
"""


# ── Z-function ───────────────────────────────
# Z[i] = length of longest substring starting at i matching a prefix of s
# Pattern matching: z(pattern + '$' + text), look for Z[i] == len(pattern)

def z_function(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


# ── KMP ──────────────────────────────────────

def kmp_prefix(s):
    """pi[i] = longest proper prefix of s[0..i] that is also a suffix."""
    n = len(s)
    pi = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        pi[i] = k
    return pi

def kmp_search(text, pattern):
    """Returns list of starting indices where pattern occurs in text."""
    s = pattern + "#" + text
    pi = kmp_prefix(s)
    m = len(pattern)
    return [i - 2 * m for i in range(2 * m, len(s)) if pi[i] == m]


# ── Polynomial Hashing ──────────────────────
# Use TWO hashes (different mods) to reduce collision probability.

class PolyHash:
    def __init__(self, s, base=131, mod=10**18 + 9):
        n = len(s)
        self.mod = mod
        self.h = [0] * (n + 1)
        self.pw = [1] * (n + 1)
        for i in range(n):
            self.h[i + 1] = (self.h[i] * base + ord(s[i])) % mod
            self.pw[i + 1] = self.pw[i] * base % mod

    def get(self, l, r):
        """Hash of s[l:r] (half-open)."""
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

# h = PolyHash(s)
# h.get(0, 3) == h.get(5, 8)  # s[0:3] == s[5:8] ?
