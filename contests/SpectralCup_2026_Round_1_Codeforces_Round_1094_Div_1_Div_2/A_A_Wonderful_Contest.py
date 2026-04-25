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
    problems = int(input())
    # print(f"test0:{problems}")
    subdivisions = (input()).split(" ")
    frequency = [False]*(100*len(subdivisions)+1)
    # print(frequency)
    frequency[0]=True
    for subdivision in subdivisions:
        coefficent = 100//int(subdivision)
        counter = coefficent
        while(counter <= 100*len(subdivisions)):
            frequency[counter] = True
            counter+= coefficent
    if(set(frequency) == {True}):
        print("Yes")
    else:
        print("No")



def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    main()
