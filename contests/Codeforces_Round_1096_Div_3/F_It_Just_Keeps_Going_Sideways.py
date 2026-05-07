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
    arr_height = list(map(int, input().split()))
    base_shift, last_populated_height = shift_amount(arr_height, arr_len)
    # print(base_shift)
    freq = [0]*(arr_len+1)
    for index, val in enumerate(last_populated_height):
        freq[index] = abs(val-arr_len)
    # print("freq",freq)
    best_shift=0
    for col in range(arr_len-1,-1,-1):
        # Remove Block
        # print("arr_height[col]",arr_height[col])
        # print("freq",freq)
        for row in range(arr_height[col],0,-1):
            freq[row]-=1
        # print("freq[arr_height[col]]",freq[arr_height[col]])
        # print("freq",freq)
        best_shift=max(freq[arr_height[col]],best_shift)
    print(base_shift+best_shift)



def shift_amount(arr,arr_len):
    shift = 0
    # Default Last Height to the end
    # This is essense the last column that height has reached
    # Initalized to last col with 0 not considered
    last_height_populated = [arr_len]*(arr_len+1)
    first_height_populated= [-1]*(arr_len+1)
    # print(range(len(arr)-1))
    for col in range(arr_len-1,-1,-1):
        # Iterate through each one and determine the last height populated
        for row in range(arr[col],0,-1):
            # Update of it existing/populated now
            last_height_populated[row]-=1
            if first_height_populated[row]==-1:
                first_height_populated[row]=col
            # Calculate Shift
            shift += max(0, last_height_populated[row]-col)
        #     print("last_height_populated", last_height_populated)
        #     print("  arr", arr)
        #     print("  col", col, "row",row)
        # print()
    return shift, last_height_populated


    # for idx in range(len(arr)-2,-1,-1):

def optimized_solve():
    col_len = int(input())
    height_arr = list(map(int, input().split()))

    # Firstly we need to know two items
    # 1. The frequency of each height (How many blocks are on each row/height)
    # 2. The height index sum (Used to help us calculate the row)
    height_freq = [0]*(col_len+2)
    height_index_sum = [0]*(col_len+2)
    for col, height in enumerate(height_arr):
        height_freq[height]+=1
        height_index_sum[height]+=col

    # Then we can calculate the row
    cubes_at_row = [0]*(col_len+2)
    index_sum_at_row = [0]*(col_len+2)
    for row in range (col_len, 0, -1):
        # Start from top to bottom
        # Iterate through rows to get the current freq of that row and top (Since they stack)
        cubes_at_row[row] = cubes_at_row[row+1]+height_freq[row]
        # The index sum of occurance accross rows (Since they stack)
        index_sum_at_row[row] = index_sum_at_row[row+1]+height_index_sum[row]

    # index_sum_at_row is critically since it determines the difference of the shift
    # Example
    #  1 0 0 0 Before Shift Sum = 0
    #  0 0 0 1 After Shift  Sum = 3
    #  Differnce is 3-0 = 3 which is the shift amount
    #  1 0 1 0 Before Shift Sum = 2
    #  0 0 1 1 After Shift  Sum = 5
    #  Differnce is 5-2 = 3 which is the shift amount
    # The utilization of the before and after showcases the shift amount!

    # For the after shift, we can calculate it since it is similar to an 1+2+3 pattern
    #  Hence cube_count * (cube_count+1) // 2 (Gauss Formula/Arthmetic Series) to get the
    #  offset pattern

    # Find the Base Shift which is the shift amount if we were to drop all the cubes at once
    base_shift = 0
    for row in range(1, col_len+1):
        if cubes_at_row[row]==0:
            # Break Early since above rows will also be 0
            break
        cube_count = cubes_at_row[row]
        # (cube_count-1)*cube_count//2 is used to calculate the 1+2+3+... pattern of the shift for each cube
        #  when they are populated in the row
        # For each row, k cubes will land at positions (len-k), (len-k+1), ... (len-1)
        # k*(len-k) is used to get the base index up repeated k (cube) times
        # k*(k-1)//2 is used to get the 0+1+2+ offset that is stacked on top of (len-k)
        # Example
        # Value 0 0 1 1
        # Index 0 1 2 3
        # k*(len-k) = 2*(4-2) = 4 = 2*cube_count
        # k*(k-1)//2 = 2*(2-1)//2 = 1
        # 2+0=2, 2+1=3
        # Hence the cubes will be at index 2 and 3 which is correct
        after_shift_sum = cube_count * (col_len - cube_count) + \
            cube_count * (cube_count - 1) // 2
        # Before Shift Sum was calculated in the previous loop
        before_shift_sum = index_sum_at_row[row]

        base_shift += after_shift_sum - before_shift_sum

    # Now we find best shift
    best_shift = 0
    for col in range(col_len):
        # Iterate through each column and get the top cube that can be removed
        top_row = height_arr[col]
        # Given that we:
        #  1. Know the row we maybe be removing the cube (from top_row)
        #  2. Know how many cubes are at that row (cubes_at_row[top_row])
        #  3. By proxy of #2, we know the index of the last cube at that row after shifting
        # We add the column since that is the benefit of it being removed
        #  The higher the column, the more beneficial it is to remove since it is closer
        #  to the end and will be shifted more
        # We give the number of cubes at that row since that is the offset of the top cube after
        #  shifting
        # We subtract the col_len since that is the last index and we want to get the difference
        #  of the shift
        pot_shift = col + cubes_at_row[top_row] - col_len
        best_shift = max(best_shift, pot_shift)

    print(base_shift+best_shift)

def main():
    T = int(input())
    for _ in range(T):
        optimized_solve()


if __name__ == "__main__":
    main()
