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
    # Rules you must always pop the first element
    # You can only multiple if the value is lower from initial
    # Only time that is useful if 1 is involved
    counter = 0
    while len(arr)!=0:
        current = arr.pop(0)
        cur_value = current
        is_one = True if current == 1 else False
        idx = 0
        while idx < len(arr):
            num = arr[idx]
            if current == 1 and num == 1:
                current *= arr.pop(idx)
            elif is_one:
                is_one = False
                current *= arr.pop(idx)
            else:
                idx += 1
        # print(f"array: {arr}")
        # print(f"current: {current}; is_one: {is_one}; idx: {idx}")
        counter = (counter+current)%676767677
        # print(f"current: {current}")
    print(counter%676767677)


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
