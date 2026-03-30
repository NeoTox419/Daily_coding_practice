#problem name: Chocolate Pickup
'''
INTUITION:
Two robots move from top row to bottom row.
At every step, both robots move simultaneously to the next row.
Each robot has 3 choices: left-diagonal, down, right-diagonal.

The total chocolates collected depends on positions of both robots.
If both land on same cell → count once, else count both.

APPROACH:
Use 3D DP (row, col1, col2):
dp[i][j1][j2] → maximum chocolates collected from row i to bottom,
                when robot1 is at column j1 and robot2 at column j2.

Recurrence:
Try all 9 possible moves for both robots.
Add current cell(s) value + best of next states.

Base Case:
If we are at last row → return grid value(s).

Use memoization to avoid recomputation.
'''
class Solution:
    def maxChocolate(self, grid):

        n = len(grid)
        m = len(grid[0])

        # Memoization table
        dp = [[[ -1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        def solve(i, j1, j2):
            # Boundary check
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            # Base case: last row
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]

            # Already computed
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            # Current cell chocolates
            if j1 == j2:
                curr = grid[i][j1]
            else:
                curr = grid[i][j1] + grid[i][j2]

            maxi = float('-inf')

            # Try all 9 combinations of moves
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    value = curr + solve(i + 1, j1 + dj1, j2 + dj2)
                    maxi = max(maxi, value)

            dp[i][j1][j2] = maxi
            return maxi

        # Start positions: (0,0) and (0,m-1)
        return solve(0, 0, m - 1)