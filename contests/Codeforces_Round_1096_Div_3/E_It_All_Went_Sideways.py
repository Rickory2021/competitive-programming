"""
Problem:  https://codeforces.com/problemset/problem/2227/E
Rating:   <RATING>
Tags:     binary search, data structures, dp, greedy
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

def optimized_solve():
    arr_len = int(input())
    arr = list(map(int, input().split()))
    base_shift, min_cascade_arr = optimized_shift_amount(arr,arr_len)
    # We now know the base shift in general and now we know how many blocks don't get moved
    # ith that we have to remove one block. What this means with an array of blocks that don't move
    #  is that since it is min, it never increases.
    # When it decrases that means that situation, blocks are blocked by a previous block or it is the one
    # This mean continuous of the same value means that most bang
    # You can think of it like removing the right most continuous same value and all the left most decrease
    #  minimium down by one (Hence Big Cascade)
    max_bundle, bundle_size, bundle_height = -1, -1, -1
    for col in range(arr_len):
        cur_val = min_cascade_arr[col]
        if bundle_height != cur_val:
            # Reset Slice
            max_bundle = max(max_bundle, bundle_size)
            bundle_size=1
            bundle_height=cur_val
        else:
            # Same Slice!
            bundle_size+=1
    # Flush out
    max_bundle = max(max_bundle, bundle_size)
    # Trim 1 since we have to remove to get best cascade
    max_bundle -= 1
    print(max_bundle+base_shift)

def optimized_shift_amount(arr_1d,arr_len):
    shift = 0
    min_cascade_arr = [0] * arr_len
    # Populate first
    # Get Minimium to cause a cascade
    min_cascade_height = arr_1d[arr_len-1]
    min_cascade_arr[arr_len-1] = arr_1d[arr_len-1]
    # print(range(len(arr)-1))
    for col in range(arr_len-2,-1,-1):
        shift+=max(0, arr_1d[col]-min_cascade_height)
        min_cascade_height = min(min_cascade_height,arr_1d[col])
        min_cascade_arr[col]=min_cascade_height
    return shift, min_cascade_arr


    # for idx in range(len(arr)-2,-1,-1):


def main():
    T = int(input())
    for _ in range(T):
        optimized_solve()


if __name__ == "__main__":
    main()
