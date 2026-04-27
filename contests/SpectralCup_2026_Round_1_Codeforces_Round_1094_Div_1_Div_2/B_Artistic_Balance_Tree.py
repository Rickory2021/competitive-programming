"""
Problem:  <URL>
Rating:   <RATING>
Tags:     <TAGS>
"""

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
    arr_len, operations = map(int, input().split())
    arr = list(map(int, input().split()))
    marked_arr = list(map(int, input().split()))
    pass


def optimized_solve():
    arr_len, operations = map(int, input().split())
    arr = list(map(int, input().split()))
    marked_idx = list(map(int, input().split()))
    """
    Core idea
    Swapping always preserves Parity (Whether a number is odd or even)
    Additionally since you can control the pivot and the radius of the rotation/Flip (Swap)
     You can swap any even number with another even number
     You can swap any odd number with another odd number
    """
    # Seperate into even and odd subsets (since index starts at 0, odds start with no offset)
    odds = arr[::2]
    evens = arr[1::2]

    # Get the count of even and odd marked indices
    odd_freq = sum(1 for idx in marked_idx if idx % 2 == 1)
    even_freq = len(marked_idx) - odd_freq
    # Reduce to when marked evens/odds are more than the actual array overflow
    odd_freq = min(len(odds), odd_freq)
    even_freq = min(len(evens), even_freq)

    # Sort Desending - This means that the end of the array is the largest and what we need
    odds_sorted = sorted(odds, reverse=True)
    evens_sorted = sorted(evens, reverse=True)

    # Discovers Negatives and sees if we can greedily save them to get lower value
    non_positives_odds_hits = sum(1 for x in odds_sorted if x >= 0)
    if odd_freq == 0:
        effective_odds_k = 0
    elif non_positives_odds_hits > 0:
        effective_odds_k = min(odd_freq, non_positives_odds_hits)
    else:
        effective_odds_k = 1

    non_positives_evens_hits = sum(1 for x in evens_sorted if x >= 0)
    if even_freq == 0:
        effective_evens_k = 0
    elif non_positives_evens_hits > 0:
        effective_evens_k = min(even_freq, non_positives_evens_hits)
    else:
        effective_evens_k = 1

    """
    Since slice is index and index starts at 0, frequency matches perfectly for cutting elements
    even/odd subset [2,1,0] with even/odd freq = 1
    [1:] = [1,0] unmarked
    """
    min_unmarked_value = sum(odds_sorted[effective_odds_k:]) + sum(evens_sorted[effective_evens_k:])
    print(min_unmarked_value)


def main():
    T = int(input())
    for _ in range(T):
        optimized_solve()


if __name__ == "__main__":
    main()
