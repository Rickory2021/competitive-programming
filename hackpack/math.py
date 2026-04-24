"""
Math — Sieve, Factorize, Modular Arithmetic, nCr, Binary Search
════════════════════════════════════════════════════════════════
MOD = 998244353 or 10**9 + 7 — know which one the problem wants!
"""
from bisect import bisect_left, bisect_right

MOD = 10**9 + 7


# ── Sieve of Eratosthenes ────────────────────

def sieve(n):
    """Returns list of primes up to n. O(n log log n)."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


# ── Prime Factorization ──────────────────────

def factorize(n):
    """Returns dict {prime: exponent}."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


# ── Modular Arithmetic ───────────────────────

def mod_pow(base, exp, mod=MOD):
    """Use built-in pow(base, exp, mod) instead."""
    return pow(base, exp, mod)

def mod_inv(a, mod=MOD):
    """Modular inverse (mod must be prime)."""
    return pow(a, mod - 2, mod)


# ── Combinatorics (precomputed factorials) ───

class Combo:
    def __init__(self, n, mod=MOD):
        self.mod = mod
        self.fact = [1] * (n + 1)
        self.inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.inv_fact[n] = pow(self.fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % mod

    def ncr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod

    def npr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[n - r] % self.mod

# combo = Combo(2 * 10**5)
# combo.ncr(10, 3)  -> 120


# ── Binary Search on Answer ─────────────────
# "What is the min/max value X such that check(X) is True?"

def bs_min(lo, hi, check):
    """Find minimum x in [lo, hi] where check(x) is True.
    Assumes: False...False True...True"""
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def bs_max(lo, hi, check):
    """Find maximum x in [lo, hi] where check(x) is True.
    Assumes: True...True False...False"""
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

def bs_float(lo, hi, check, iters=100):
    """For continuous domains (geometry, etc.)."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        if check(mid):
            hi = mid
        else:
            lo = mid
    return lo

# bisect_left(arr, x)   -> first index where arr[i] >= x
# bisect_right(arr, x)  -> first index where arr[i] > x
# Count of x in sorted arr: bisect_right(arr, x) - bisect_left(arr, x)
