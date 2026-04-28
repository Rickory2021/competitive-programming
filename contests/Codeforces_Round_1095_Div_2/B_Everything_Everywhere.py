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
    arr_len = int(input())
    arr = list(map(int, input().split()))
    # It is not possible to have diff = gcd of a permutation with an array larger than 2
    # After all, just have the gcd be any number the smallest factor different is usually 2
    # This means that diff can't even work for [1,2,4] which is the smallest, so only 2
    #  combinations is good
    # Sicne it is asking for sub array, no need for combinations/sorting
    matches = 0
    for start_idx in range(arr_len - 1):
        # To allow space for two elements with +1
        matches += abs(arr[start_idx]-arr[start_idx+1]) == gcd(arr[start_idx], arr[start_idx+1])
    print(matches)

def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
