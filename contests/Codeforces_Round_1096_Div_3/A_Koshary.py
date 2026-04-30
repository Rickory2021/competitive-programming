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
    arr = list(map(int,input().split()))
    x,y=arr[0],arr[1]
    ans = "NO" if x%2==1 and y%2==1 else "YES"
    print(ans)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
