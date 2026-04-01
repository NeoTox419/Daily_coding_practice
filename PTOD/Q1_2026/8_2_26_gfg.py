#porblem name: Maximum Product Subarray
'''
------------------------------------------------------------
Problem:
Given an array arr[] that contains positive and negative
integers (may contain 0 as well), find the maximum product
that we can get in a subarray of arr[].
------------------------------------------------------------
First Intuition:

A simple idea is to try all possible subarrays, calculate
the product of each subarray, and keep track of the maximum.

But this brute-force approach takes O(n^2) subarrays and
computing product each time can make it O(n^3), which is
too slow.

Also, negative numbers make things tricky:
- A negative number can turn a small product into a large one
- Zero breaks the product chain
------------------------------------------------------------
Approach:

We use a dynamic programming approach.

Key idea:
At every index, we track:
1. max_prod: maximum product ending at this index
2. min_prod: minimum product ending at this index

Why track minimum?
Because multiplying a negative number with the minimum
(negative) product can give a new maximum.

Steps:
- Initialize max_prod, min_prod, and result with first element
- Iterate through the array from index 1
- If current element is negative, swap max_prod and min_prod
- Update max_prod and min_prod
- Update result

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def maxProduct(self, arr):
        if not arr:
            return 0

        max_prod = arr[0]
        min_prod = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            curr = arr[i]

            # If current element is negative, swap
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(curr, max_prod * curr)
            min_prod = min(curr, min_prod * curr)

            result = max(result, max_prod)

        return result
