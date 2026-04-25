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
    len = int(input())
    arr = list(map(int, input().split()))
    sorted_arr= sorted(list(arr.copy()))
    # print(f"sorted_arr:{sorted_arr}")
    sorted_arr= sorted(sorted_arr)

    median = sorted_arr[len//2]

    diff = 0
    lower_bound_count = 0
    upper_bound_count = 0
    median_count = 0
    subarr_counter = 0
    for num in arr:
        if num == median:
            median_count+=1
        elif num < median:
            lower_bound_count+=1
        else:
            upper_bound_count+=1
        if (lower_bound_count + upper_bound_count + median_count) % 2 == 1:
            # odd length
            if median_count > 0:
                # has median
                if (lower_bound_count == upper_bound_count) \
                    or (lower_bound_count > upper_bound_count and lower_bound_count - upper_bound_count <= median_count) \
                    or (upper_bound_count > lower_bound_count and upper_bound_count - lower_bound_count <= median_count):
                    # equal number of upper and lower bounds
                        subarr_counter+=1
                        lower_bound_count = 0
                        upper_bound_count = 0
                        median_count = 0
        print(f"num:{num},lower_bound_count:{lower_bound_count},upper_bound_count:{upper_bound_count},median_count:{median_count},subarr_counter:{subarr_counter}")
    # Clean up any remaining bounds
    if lower_bound_count + upper_bound_count + median_count > 0:
        diff = abs(lower_bound_count - upper_bound_count)-median_count
        if diff > 0:
            subarr_counter-=diff
        # subarr_counter-=abs(lower_bound_count - upper_bound_count)-median_count
        # Uses up the remaining median counts to balance out the upper and lower bounds
        # median used to balance out where needed
        if subarr_counter < 0:
            subarr_counter=1
            # Edge case where leftover could not score a sub array
    print(subarr_counter)
def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
