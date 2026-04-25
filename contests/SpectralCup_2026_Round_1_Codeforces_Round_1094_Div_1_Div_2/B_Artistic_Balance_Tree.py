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


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
