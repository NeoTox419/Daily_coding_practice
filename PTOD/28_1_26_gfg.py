#Problem Name: Count subset with Target sum II

'''
intuation
--------
We are asked to count how many subsets of the given array have a sum
exactly equal to k.

A subset problem usually hints at Dynamic Programming because:
- For every element, we have two choices: include it or exclude it.
- The same subproblems (index, remaining sum) repeat.

This is a variation of the classic "Subset Sum" problem, but instead of
checking if a subset exists, we count how many such subsets exist.
'''

'''
apporach
---------
We use Dynamic Programming where:
dp[s] = number of subsets with sum equal to s.

Initialization:
- dp[0] = 1 because there is exactly one subset (empty subset) with sum 0.

Transition:
- For each number num in arr:
    Traverse dp from k down to num:
        dp[s] += dp[s - num]

Why backward traversal?
- To avoid reusing the same element multiple times in a single subset.

Final Answer:
- dp[k] will store the count of subsets whose sum is exactly k.

Time Complexity:  O(n * k)
Space Complexity: O(k)
'''

class Solution:
    def countSubset(self, arr, k):
        min_sum = 0
        max_sum = 0

        for num in arr:
            if num < 0:
                min_sum += num
            else:
                max_sum += num

        if k < min_sum or k > max_sum:
            return 0

        offset = -min_sum
        size = max_sum - min_sum + 1

        dp = [0] * size
        dp[offset] = 1

        for num in arr:
            new_dp = dp[:]
            for s in range(size):
                if dp[s]:
                    ns = s + num
                    if 0 <= ns < size:
                        new_dp[ns] += dp[s]
            dp = new_dp

        return dp[k + offset]


