"""
Minokowski Sum
https://cp-algorithms.com/geometry/minkowski.html
https://en.wikipedia.org/wiki/Minkowski_addition

Updated: 2026-04-26

Core Idea
Say you have two sets of points A and B.
The Minkowski sum A + B is the set of all sums.
A + B = {a + b | a ∈ A, b ∈ B}

In essense, find all sum combinations of points in A and B.

This can be further chained to find
A + B + C = { a + b + c | a ∈ A, b ∈ B, c ∈ C }

Goal: Pick one value from each group, and totals/positions are reachable

Example:
    1D Examples:
        - Can you make total X using coins (denominations) A and B?
        - What scores are possible if each problem is weighted by A and B?
        - Subset sums with group/bounded items (e.g. 0-1 knapsack)?
    2D Examples:
        - Can convex shape A movbe through a gaph without hitting convex shape B?
        - What position are reachable by summing displacement vectors?
        - What position are reachable for a robot motion planning problem?

Symptoms:
    - Multiple independnt groups where you need to pick one value from each group
    - Can you achieve every value in a range
    - What totals are possible
    - Bounded Coin (Change Problem) or Bounded 0-1 Knapsack (How much can I carry?) with quantity constraints
    - Two convex shapes needed to be "added" or "inflated" to find reachable positions
"""

# Pattern 1: 1D Minkowski Sum (Bitset Sums)
"""
When it comes to a 1D Minkowski sum problems, they often boil down to a variation of the coin change problem
 or subset sum problem.
A bitset can be used to efficiently compute the Minkowski sum of two sets of integers.
Bitsets is just an integer that is used as an array of True/False values through the use of binary operations
We can treat each bit as a visited state where it is either True (1) or False (0)

In essense we can represent a visted array as a number acting as a bitset where operations are more efficent

What are Bit Sets?
    Example:
        {0, 3, 5} is represented as 0b101001 (or 41 in decimal) because we can make the sums 0, 3, and 5.
        decimal 41 = binary 101001
        Written out with positions labeled:
            bit position:  5  4  3  2  1  0
            bit value:     1  0  1  0  0  1

    Advantages of bitsets over Lists or Sets:
        Bitwise Operations are Fast: Bitwise operations (AND, OR, XOR, shifts) are extremely fast
        and can process multiple bits in parallel.

        Example:
            1. OR (|) = set union
                {0, 3} | {1, 3, 5}  =>  {0, 1, 3, 5}
                In binary:  001001 | 101010 = 101011
                Find all sums that can be made by either A or B, or both.

            2. AND (&) = set intersection
                {0, 3, 5} & {3, 4, 5}  =>  {3, 5}
                In binary:  101001 & 111000 = 101000
                Find all sums that can be made by both A and B.

            3. LEFT SHIFT (<<) = add a constant to every element (>> subtract a constant from every element)
                {0, 3, 5} << 2  =>  {2, 5, 7}
                In binary:  101001 << 2 = 10100100
                Find all sums that can be made by adding 2 to every element in the set.

            4. LEFT SHIFT (<<) = to check existance/membership of a sum
                Is 3 in {0, 3, 5}?  =>  41 & (1 << 3) = 41 & 8 = 8 (truthy) => YES
                101001 & (000001 << 3) => 101001 & (001000)
                bit position:  5  4  3  2  1  0
                bit value:     1  0  1  0  0  1
                operator:      &  &  &  &  &  &
                bit value:     0  0  1  0  0  0
                Result:        0  0  1  0  0  0 (8 in decimal) != 0 = YES

        Python, bit ints does operations on all N bits in chunks of 64 at once (parallel of 64 bits at a time)
        Where as a boolean Dyanamic Programing (DP) array like dp = [False] * (max_sum + 1) would require
        O(max_sum) time to update each state.

    Connecting with Minkowski Sums:
        Given Minkowski sum A + B = { a + b | a ∈ A, b ∈ B }, find all sums that can be made by picking one element
         from A and one element from B.
        Do it by representing the sums of A and B as bitsets, where each bit position represents whether a particular
         sum is achievable.
            This can be done by Initializea bitset for A and have B iterate with utilization of bitwise operations

        A + B = { a + b | a ∈ A, b ∈ B}
        A + B = { (A << b_0) | (A << b_1) | (A << b_2) | ... for b_i in B }
"""


def minkowski_sum_1d_2_bitset(A, B):
    """
    Example:
            A = {0, 3, 6}   (2 items worth 3 units)
            B = {0, 5, 10}  (2 items worth 5 units)

            Max possible total = 6 + 10 = 16

            A + B = { a + b | a ∈ A, b ∈ B}
            A + B = { (A << b_0) | (A << b_1) | (A << b_2) | ... for b_i in B }
    """
    # 1. Initializebitset for A:
    """
    (0b1) because we can make the sum 0 by picking nothing from all Sets.
    Written out with positions labeled:
        bit position:  ... 3  2  1  0
        bit value:     ... 0  0  0  1
    """
    reachable = 1

    # 2. For each group in A,
    #    Makes a new to previous results does not muddy the current result
    new_reachable = 0
    for val in A:
        """
        << mean to add val to every element in the new reachable sums
        |= means union with what we already found
        Together it means that we can make new sums by adding val to every sum we could already make,
            and we combine that with the sums we could already make
        """
        new_reachable |= reachable << val

    # 3. Update reachable sums with the new reachable sums after processing the current group
    reachable = new_reachable

    # 4. For each group in B,
    #    Same Operation as the above
    new_reachable = 0
    for val in B:
        new_reachable |= reachable << val
    # 3. Update reachable sums with the new reachable sums after processing the current group
    reachable = new_reachable

    return reachable


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


# ── TODO: 2D Minkowski Sum (Convex Polygons) ──
# Add when tackling geometry problems.
# Reference: https://cp-algorithms.com/geometry/minkowski.html
