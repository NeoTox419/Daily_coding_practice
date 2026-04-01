"""
    INTUITION:
    -----------
    A permutation means arranging all elements of the array in every possible order.
    Since all elements are unique, we don't have to worry about duplicates.

    Think of building permutations step by step:
    - Fix one element at the current position
    - Recursively generate permutations for the remaining elements
    - Backtrack to try the next possibility

    This is a classic example of backtracking.    
"""

"""
    APPROACH:
    ----------
    1. Use recursion and backtracking.
    2. Swap the current index element with every element after it.
    3. Recursively permute the rest of the array.
    4. Once we reach the end, store a copy of the current arrangement.
    5. Backtrack by swapping back to restore the original state.
"""

"""
    SOLUTION:
    ----------
    Time Complexity: O(n! * n)
    Space Complexity: O(n!) for storing permutations
"""

class Solution:
    def permuteDist(self, arr):
        
        result = []

        def backtrack(index):
            # Base case: if we've fixed all positions
            if index == len(arr):
                result.append(arr[:])  # store a copy
                return

            # Try placing each remaining element at the current index
            for i in range(index, len(arr)):
                arr[index], arr[i] = arr[i], arr[index]  # swap
                backtrack(index + 1)                      # recurse
                arr[index], arr[i] = arr[i], arr[index]  # backtrack

        backtrack(0)
        return result
