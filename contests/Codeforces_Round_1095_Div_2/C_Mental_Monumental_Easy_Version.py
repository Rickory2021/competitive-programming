"""
Problem:  https://codeforces.com/problemset/problem/2226/C
Rating:   <RATING>
Tags:     binary search, data structures, greedy, math, two pointer
"""
# ── TODO: Add to HackPack Binary Search on the Answer ──
# - https://codeforces.com/blog/entry/143038
# - https://cp-algorithms.com/num_methods/binary_search.html

import sys
from sys import stdin
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop, heapify
from math import gcd, inf, ceil, floor, log2, isqrt
from functools import lru_cache
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def solve():
    """
    The key goal is to try to create a stair case from 0 to x in anyway possible with mod
    The key is to revert modulo into getting remainder consitency
    remainder = a - (coefficent * floor(a/coefficent))
    How to reverse to get n?
    """
    arr_len = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(arr)
    # print(f"sorted_arr: {sorted_arr}")
    # Loop from bottom up goal is to get as low as possible
    missing_min = list(range(arr_len))
    checked = []
    idx = 0
    while len(sorted_arr)!=0:
        current = sorted_arr.pop(0)
        used = False
        for miss_idx, missing in enumerate(missing_min):
            # print(f"Checking coefficent for: {missing} with {current}")
            if does_coefficent_exist(current, missing):
                # print(f"found coefficent for: {missing} with {current}")
                missing_min.pop(miss_idx)
                used=True
                break
        if not used:
            checked.append(current)
        # print(f"sorted_arr: {sorted_arr}")
        # print(f"checked_arr: {checked}")
        # print(f"missing_min: {missing_min}")
        # print
    print(missing_min[0] if len(missing_min)>0 else arr_len)

    #     current = sorted_arr[idx]
    #     missing_min.append(idx)
    #     print(f"before check: {missing_min}")
    #     for miss_idx, missing in enumerate(missing_min):
    #         print(f"Checking coefficent for: {missing} with {current}")
    #         if does_coefficent_exist(current, missing):
    #             print(f"found coefficent for: {missing} with {current}")
    #             missing_min.pop(miss_idx)
    #             sorted_arr[idx]=missing
    #             used = True
    #             break
    #     if used:
    #         idx+=1
    #         used = False
    #     print(f"missing: {missing_min}")
    #     print(f"sorted_arr {sorted_arr}")
    #     print()

    # print(missing_min[0] if len(missing_min)>0 else arr_len)

def does_coefficent_exist(a, remainder):
    if a == remainder:
        return True
    if a < remainder:
        return False
    coefficent = 1
    while coefficent <= isqrt(a - remainder) + 1:
        if remainder == a % coefficent:
            return True
        coefficent += 1
    return False

def optimized_solve():
    """
    Ground Rules:
     Given a remainder = a - (coefficent * floor(a/coefficent)) where we have to find
      Whether remainder can be found in a, we have two quick ways to do it
        1. If a==remainder, coefficent is garenteed
        2. If a>2r, if we subtract it once, then remainder of the subtraction is easy
            Example:
             a = 10, r=3 where 10>2(3)
             This means coefficent of 7 (10-3) always ensure the remainder is possible
        The largest a>2r is the best remainder you can get. Smaller remainders will also appear,
         but technically, since we are looking for the highest remainder, since
            a = 10 has remainders of 10, 4, 3, 2, 1, 0

    With the above ground rules, we can safely determine the possible remainders a number can get

    The goal is to utilize the smallest numbers to get the highest remainders. when doing that,
     1. Since larger remainders are harder to get using smaller numbers, we want to save
        the largest numbers to give more chances of larger numbers to hit
     2. Overall, in precedence, a==r is best and a>2r where r is the highest is second best.
        This means that we want the smallest a that still satisfies a>2r when a!=r
     3. When we get to a MEX check where it couldn't be found after iterating through the
        largest number, then it is a wrap

    Binary Search:
     We can't greedily claim all a==r upfront because we might waste
      elements on remainders beyond our actual MEX
     Example:
      [0, 0, 0, 3] claiming 3 as a==r for r=3 wastes it,
      when it could flexibly cover r=1 (3 > 2*1)
     Instead, binary search on k and only claim specialists for [0, k-1]
    """
    arr_len = int(input())
    arr = list(map(int, input().split()))

    # Get Frequency of items for a==r lookups
    counts = Counter(arr)

    # Binary search on k: find the largest k where feasible(k) is True
    #  low = definitely achievable, high = maybe achievable
    #  When low == high, that's our answer
    low = 0
    high = arr_len
    while low < high:
        mid = (low + high + 1) // 2
        if feasible(mid, counts):
            # MEX = mid works, try higher
            # All lower mid can get to Max MEX without higher a==r
            low = mid
        else:
            # MEX = mid fails, try lower
            # Lower k to free up larger a==r if possible
            high = mid - 1
    print(low)

def feasible(k, original_counts):
    """
    Check if MEX = k is achievable
    We only claim a==r for r in [0, k-1] so we don't waste elements
     on remainders we aren't even testing
    """
    # Copy counts so we don't mutate between binary search iterations
    counts = Counter(original_counts)

    # Pass 1: Claim specialists (a == r) only for r in [0, k-1]
    #  These elements can ONLY serve their one specific remainder
    #  so they get priority before flexible elements
    matched = set()
    for r in range(k):
        if counts[r] > 0:
            counts[r] -= 1
            matched.add(r)

    # Rebuild remaining elements after specialists are removed
    remaining = []
    for val, cnt in counts.items():
        remaining.extend([val] * cnt)
    # Sort ascending: smallest elements first, saved for easiest remainders
    remaining.sort()

    # Pass 2: Two-pointer sweep for unmatched remainders
    #  We go 0 to k-1 (ascending) with ascending elements
    #  Small remainders are easy (a > 2r threshold is low)
    #  Large remainders are hard (need bigger elements)
    #  Elements that fail current remainder (a <= 2r) might still fail
    #   future harder remainders, so we skip past them
    idx = 0
    for r in range(k):
        if r in matched:
            # Already covered by a a==r, skip
            continue
        while idx < len(remaining) and remaining[idx] <= 2 * r:
            # This element can't satisfy a > 2r, skip it
            idx += 1
        if idx >= len(remaining):
            # No elements left to cover this remainder, k is not feasible
            return False
        # Consume the element so it isn't reused
        idx += 1
    return True

def main():
    T = int(input())
    for _ in range(T):
        optimized_solve()


if __name__ == "__main__":
    main()
