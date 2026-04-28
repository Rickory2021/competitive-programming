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

def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
