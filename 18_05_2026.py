#Problem name: Maximum Sum problem
'''
Intuition:
For every number n, we have two choices:

1. Do not break the number
    -> value = n

2. Break the number into:
        n//2, n//3, n//4
    and recursively calculate their best possible values.
    -> value = f(n//2) + f(n//3) + f(n//4)

We choose the maximum among these two choices.

Example:
n = 12

Without breaking:
    value = 12

With breaking:
    f(6) + f(4) + f(3)
    = 6 + 4 + 3
    = 13

So answer = 13.


Approach:
- Use recursion to calculate the maximum obtainable value.
- Since many subproblems repeat, use memoization (DP).
- Store already computed answers in a dictionary.

Recursive Relation:
    f(n) = max(
                n,
                f(n//2) + f(n//3) + f(n//4)
                )

Time Complexity:
    O(number of unique states)

Space Complexity:
    O(number of recursive states)
'''
class Solution:
    def maxSum(self, n):
        dp = {}

        def solve(x):
            if x == 0:
                return 0

            if x in dp:
                return dp[x]

            dp[x] = max(
                x,
                solve(x // 2) + solve(x // 3) + solve(x // 4)
            )

            return dp[x]

        return solve(n)