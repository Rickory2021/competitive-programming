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
    length = input()
    text = list(input().strip())
    # If odd it is false
    freq = Counter(text)
    invalid = False
    # print(freq, freq["("],freq[")"])
    if freq["("]!=freq[")"]:
        invalid = True
    print("YES" if not invalid else "NO")


def validate(text):
    open = 0
    invalid = False
    while len(text)!=0:
        character = text.pop(0)
        open+= 1 if character == "(" else -1
        if(open < 0):
            invalid=True
            break
    if open!=0:
        invalid=True
    print("YES" if not invalid else "NO")

def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
