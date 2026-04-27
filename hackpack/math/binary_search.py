"""
Binary Search Patterns
──────────────────────
The two patterns you actually need in contests.
"""

from bisect import bisect_left, bisect_right


# ── Pattern 1: Binary search on answer ──
# "What is the minimum/maximum value X such that check(X) is True?"


def binary_search_min(lo, hi, check):
    """Find minimum x in [lo, hi] where check(x) is True.
    Assumes: check is monotonic — False...False True...True
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def binary_search_max(lo, hi, check):
    """Find maximum x in [lo, hi] where check(x) is True.
    Assumes: check is monotonic — True...True False...False
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2  # round up to avoid infinite loop
        if check(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


# ── Pattern 2: Binary search on floats ──


def binary_search_float(lo, hi, check, eps=1e-9):
    """For continuous domains (geometry, etc.)."""
    for _ in range(100):  # 100 iterations ≈ 10^-30 precision
        mid = (lo + hi) / 2
        if check(mid):
            hi = mid
        else:
            lo = mid
    return lo


# ── Built-in bisect shortcuts ──
# bisect_left(arr, x)   -> first index where arr[i] >= x
# bisect_right(arr, x)  -> first index where arr[i] > x
# Count of x in sorted arr:  bisect_right(arr, x) - bisect_left(arr, x)

# ── Example: "Can we split array into k subarrays each with sum <= X?" ──
# def check(max_sum):
#     count, cur = 1, 0
#     for a in arr:
#         if cur + a > max_sum:
#             count += 1
#             cur = a
#         else:
#             cur += a
#     return count <= k
# ans = binary_search_min(max(arr), sum(arr), check)
