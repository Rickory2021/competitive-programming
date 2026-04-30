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
    # Great 2D Space
    arr_2d = []
    for hit in arr:
        arr_2d.append([[True]*hit+[False]*(arr_len-hit)])
    rotated = list(zip(*arr_2d[::-1]))
    # for row in rotated:
        # print(*row)
    # print(rotated[0][0][0])

    base_shift = shift_amount(rotated,arr_len)
    # print(shift_amount(rotated,arr_len))

    # print(rotated)
    # Do Slices
    # above slice on the last occurance = amount move -1 (From removal)
    # Get Frequency + Last Index
    latest=[-1]*(arr_len+1)
    for idx,val in enumerate(arr):
        if latest[val]<idx:
            latest[val]=idx
    # Go through and do slicing
    best_shift=0
    # print(latest)
    for value, latest_idx in enumerate(latest):
        shift =0
        if latest_idx==-1:
            # Didn't Appear
            continue
        # Value = Row; latest = colum to check backwards
        for col in range(latest_idx-1,-1,-1):
            # print("col", col, "row", value)
            if rotated[0][col][value-1] == True:
                shift+=1
        best_shift=max(best_shift,shift)
    # print("base_shift",base_shift)
    print(best_shift+base_shift)

    # Now do slice
    # for


def shift_amount(arr,arr_len):
    shift = 0
    # print(range(len(arr)-1))
    for row in range(arr_len):
        is_free=False
        for col in range(arr_len-1,-1,-1):
            # Start Right
            if not is_free:
                if arr[0][col][row] == False:
                    # Empty
                    is_free=True
            else:
                if arr[0][col][row] == True:
                    shift+=1

    return shift


    # for idx in range(len(arr)-2,-1,-1):


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
