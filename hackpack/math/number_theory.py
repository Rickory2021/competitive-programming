"""
Number Theory — Sieve, Modular Arithmetic, GCD/LCM, Fast Pow
─────────────────────────────────────────────────────────────
MOD = 998244353 or 10**9 + 7 — know which one the problem wants!
"""

MOD = 10**9 + 7


def sieve(n):
    """Returns list of primes up to n. O(n log log n)."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def factorize(n):
    """Prime factorization. Returns dict {prime: exponent}."""
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


def mod_pow(base, exp, mod=MOD):
    """Fast modular exponentiation. Use built-in pow(base, exp, mod) instead."""
    return pow(base, exp, mod)


def mod_inv(a, mod=MOD):
    """Modular inverse (mod must be prime). a^(-1) mod p = a^(p-2) mod p."""
    return pow(a, mod - 2, mod)


# ── Precomputed factorials for nCr ──
class Combo:
    """Precompute factorials for fast nCr mod p."""

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


# ── Usage ──
# primes = sieve(10**6)
# combo = Combo(2 * 10**5)
# combo.ncr(10, 3)  -> 120
# mod_inv(5)        -> inverse of 5 mod 10**9+7
