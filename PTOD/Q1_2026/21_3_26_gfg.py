#poblem name: Number of BST from array
'''
INTUITION:
-----------
For any chosen root arr[i], all elements smaller than it must go to the left subtree,
and all elements greater than it must go to the right subtree.

Since all elements are distinct, the structure of BST depends only on:
- how many nodes go to the left
- how many nodes go to the right

If:
    L = number of elements smaller than arr[i]
    R = number of elements greater than arr[i]

Then:
    Number of unique BSTs = (number of BSTs with L nodes) * (number of BSTs with R nodes)

The number of unique BSTs that can be formed with n nodes is given by the
Catalan Number:
    C[n] = sum(C[i] * C[n-1-i]) for i in range(n)

APPROACH:
-----------
1. Precompute Catalan numbers up to n using DP.
2. For each element arr[i]:
    - Count how many elements are smaller (L)
    - Count how many are greater (R)
    - Answer = C[L] * C[R]
3. Return the result array.

Time Complexity:
    O(n^2) for counting smaller elements (can be optimized by sorting)

Optimized Approach:
    - Sort the array
    - The index in sorted array directly gives L
    - R = n - index - 1
    → Reduces complexity to O(n log n)
'''
class Solution:
    def countBSTs(self, arr):
        n = len(arr)

        # Step 1: Precompute Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = 1
        catalan[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Step 2: Sort array to determine ranks
        sorted_arr = sorted(arr)
        index_map = {val: i for i, val in enumerate(sorted_arr)}

        # Step 3: Compute result
        result = []
        for val in arr:
            L = index_map[val]
            R = n - L - 1
            result.append(catalan[L] * catalan[R])

        return result