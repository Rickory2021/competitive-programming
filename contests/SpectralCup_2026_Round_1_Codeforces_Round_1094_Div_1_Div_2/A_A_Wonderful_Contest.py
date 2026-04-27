"""
Problem:  https://codeforces.com/problemset/problem/2222/A
Rating:   <RATING>
Tags:     brute force, math
Viewed:   2026-04-26
"""

import sys

input = sys.stdin.readline


def solve():
    problems = int(input())
    # print(f"test0:{problems}")
    subdivisions = (input()).split(" ")
    frequency = [False] * (100 * len(subdivisions) + 1)
    # print(frequency)
    frequency[0] = True
    for subdivision in subdivisions:
        coefficent = 100 // int(subdivision)
        counter = coefficent
        while counter <= 100 * len(subdivisions):
            frequency[counter] = True
            counter += coefficent
    if set(frequency) == {True}:
        print("Yes")
    else:
        print("No")


def optimized_solve():
    # Get Inputs
    problems = int(input())
    subdivisions = map(int, (input()).split(" "))
    max_score = problems * 100

    # Generate Sets of reachable scores per problem based on subdivisions
    Sets = []
    for subdivision in subdivisions:
        # Each problem can be worth 0, coefficent, 2*coefficent, ..., up to 100
        coefficent = 100 // int(subdivision)
        counter = 0
        Set = set()
        while counter <= 100:
            # Maxed out at 100 because we can't get more than 100 points per problem,
            #  and we don't need to consider more than that
            Set.add(counter)
            counter += coefficent
        Sets.append(Set)

    reachable = minkowski_sum_1d_bitset(Sets)
    print("Yes" if reachable == (1 << (max_score + 1)) - 1 else "No")


def minkowski_sum_1d_bitset(Sets):
    """
    Example:
            A = {0, 3, 6}   (2 items worth 3 units)
            B = {0, 5, 10}  (2 items worth 5 units)
            C = {0, 2, 4}   (2 items worth 2 units)

            Max possible total = 6 + 10 + 4 = 20

            A + B + C= { a + b + C | a ∈ A, b ∈ B, c ∈ C}
            X = A + B = { (A << b_0) | (A << b_1) | (A << b_2) | ... for b_i in B }

            A + B + C = X + C = { (X << c_0) | (X << c_1) | (X << c_2) | ... for c_i in C }
    """
    # Initializebitset
    """
    (0b1) because we can make the sum 0 by picking nothing from all Sets.
    Written out with positions labeled:
        bit position:  ... 3  2  1  0
        bit value:     ... 0  0  0  1
    """
    reachable = 1

    # For Each Set,
    for Set in Sets:
        # Makes a new to previous results does not muddy the current result
        new_reachable = 0
        for val in Set:
            """
            << mean to add val to every element in the new reachable sums
            |= means union with what we already found
            Together it means that we can make new sums by adding val to every sum we could already make,
                and we combine that with the sums we could already make
            """
            new_reachable |= reachable << val

        # Update reachable sums with the new reachable sums after processing the current group
        reachable = new_reachable

    return reachable


def main():
    T = int(input())
    for _ in range(T):
        optimized_solve()


if __name__ == "__main__":
    main()
