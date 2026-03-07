'''
INTUITION
---------
Each die can contribute a value from 1 to m. When we throw n dice, the total
sum is the addition of values obtained from all dice. We want to count how many
different combinations of outcomes produce a total sum equal to x.

A brute force approach would try all possible outcomes (m^n possibilities),
but that becomes very large when n grows. Instead, we observe overlapping
subproblems and use Dynamic Programming.

Key idea:
Let dp[i][s] represent the number of ways to get sum s using i dice.

For the i-th die, we can choose any face value from 1 to m. If we choose value f,
then the remaining sum (s - f) must be formed using the previous (i - 1) dice.

So:
dp[i][s] = sum(dp[i-1][s-f]) for all f in [1, m] where s-f >= 0

Base case:
dp[0][0] = 1 (0 dice can make sum 0 in exactly one way)

Finally, dp[n][x] will give the number of ways to get sum x using n dice.

APPROACH
--------
1. Create a 2D DP table of size (n+1) x (x+1).
2. Initialize dp[0][0] = 1.
3. For each number of dice from 1 to n:
      For each possible sum from 1 to x:
          Try all face values from 1 to m.
          If s - face >= 0:
              add dp[i-1][s-face] to dp[i][s].
4. Return dp[n][x].

Time Complexity:
O(n * x * m)

Space Complexity:
O(n * x)
'''

class Solution:
    def noOfWays(self, m, n, x):
        dp = [[0]*(x+1) for _ in range(n+1)]
        
        dp[0][0] = 1
        
        for dice in range(1, n+1):
            for s in range(1, x+1):
                ways = 0
                for face in range(1, m+1):
                    if s - face >= 0:
                        ways += dp[dice-1][s-face]
                dp[dice][s] = ways
        
        return dp[n][x]