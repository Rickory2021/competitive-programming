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
    # Palidromes in this situation must always start from 0
    # The two ways to make a palidrome with 0 as basis is
    #  1. if 0 is center (1 Zero)
    #  2. if 0 is at the end (2 Zero)
    arr_len = int(input())*2
    arr = list(map(int, input().split()))
    zero_indices = [idx for idx, val in enumerate(arr) if val == 0]

    max_mex = expand_palidrome(arr_len, arr,zero_indices[0],zero_indices[1]+1,arr_len//2)

    # print("HI")
    # Now do the Center (One at a time)
    for zero_index in zero_indices:
        mex = expand_palidrome(arr_len, arr,zero_index,zero_index+1,arr_len//2)
        max_mex = max(max_mex,mex)
        # print("zero_index", zero_index, "arr_len", arr_len)
        # For each Center
        # for radius in range(arr_len//2+1):
        #     low_bound, high_bound = zero_index-radius, zero_index+radius
        #     # print("bounds", low_bound, high_bound)
        #     # print(low_bound, high_bound)
        #     if low_bound <0 or high_bound >=arr_len:
        #         # if out of bounds
        #         break
        #     else:
        #         new_arr = arr[low_bound:high_bound+1]
        #         # print(new_arr)
        #         validate = validate_palidrome(len(new_arr), new_arr, arr_len//2)
        #         if validate[0]:
        #             # print("validate[0]", validate[0], "validate[1]",validate[1])
        #             mex=get_mex(validate[1])
        #             if max_mex < mex:
        #                 max_mex = mex
        #         else:
        #             break
    print(max_mex)

def validate_palidrome(arr_length, array, max):
    # print("validtaing")
    # print(arr_length, array)
    freq=[False]*max
    for idx in range(arr_length//2+1):
        # print(array, idx, -idx-1)
        if(array[idx]!=array[-idx-1]):
            return False, -1
        freq[array[idx]] = True
        # print(array[idx], idx)
    return True, freq

def expand_palidrome(arr_len, arr, start_index, end_index, max):
    first_split = arr[start_index:end_index]
    # print("first_split",first_split)
    validate = validate_palidrome(len(first_split), first_split, max)
    # Check first one
    # print(validate)
    if not validate[0]:
        return 0
    mex_max = get_mex(validate[1])
    # print("mex_max after first", mex_max, "start_index",start_index,"end_index",end_index)
    freq = validate[1]

    for radius in range(arr_len//2+1):
        low_bound, high_bound = start_index-radius, end_index+radius-1
        # print("bounds", low_bound, high_bound)
        # print(low_bound, high_bound)
        if low_bound <0 or high_bound >=arr_len:
            # if out of bounds
            break
        else:
            val1 = arr[low_bound]
            val2 = arr[high_bound]
            if val1==val2:
                freq[val1]=True
            else:
                break
            # print("val1",val1,"val2",val2,"radius",radius,"freq",freq)
    return get_mex(freq)

def get_mex(arr):
    # print("get_mex arr", arr)
    for idx in range(len(arr)):
        if not arr[idx]:
            # If missing then that is max
            return idx
    # If it passes [0,1,2] would now give
    return len(arr)

def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
