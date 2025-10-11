"""
Trying to reframe the problem to make it easier to think about (for a grid of size n):
- You only ever have 2 options, to either go right, or go down.
- If you reach the end of the grid in one direction, you have to go the other way till the corner.
- At the end, you have to have gone both right and down n times.
So another way of asking that question is:
    How many unique sequences of n As and n Bs can you form?
This is now a permutation problem. How many permutations are there for n As and nBs.
Tricky thing is that there are repeats allowed as objects are not distinct.
"""
from GeneralFunctions import permutation_count

ANSWER = 137846528820
INPUT = 20


def main(n):
    """Find the number of valid orthogonal paths through a grid. Solved as a permutations problem."""
    return permutation_count("A"*20+"B"*20, repeats=True, perm_string_length=2*n)


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The number of different routes for a {INPUT}x{INPUT} grid is {answer}")
