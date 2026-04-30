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
    # Greedy = have 2&3 factor on left 2 on left and 3 on right
    n = int(input())
    arr = list(map(int, input().split()))
    double_factor=[]
    three_factor=[]
    two_factor=[]
    no_factor=[]
    for num in arr:
        two_mod = num%2==0
        three_mod = num%3==0
        if two_mod and three_mod:
            double_factor.insert(0,num)
        elif two_mod:
            two_factor.insert(0,num)
        elif three_mod:
            three_factor.insert(0,num)
        else:
            no_factor.insert(0,num)
    ans = []
    ans.extend(double_factor)
    ans.extend(two_factor)
    ans.extend(no_factor)
    ans.extend(three_factor)
    print(*ans)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
