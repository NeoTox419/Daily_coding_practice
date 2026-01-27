''' 
intuition
We try to form the word by walking through the grid.
From any cell matching the first character, we move up, down, left, right, matching the next characters one by one.

If a path stops matching or goes out of bounds, we backtrack and try a different direction.
Each cell can be used only once per path, so we temporarily mark it as visited.
''' 

''' 
approach 
Loop through every cell in the matrix.
When a cell matches word[0], start a DFS from there.

DFS parameters:
current position (i, j)
index k of the current character in word

Base case:
if k == len(word), the whole word is found → return True

Stop DFS if:
out of bounds
character mismatch
cell already visited
Mark the cell as visited.
Explore all 4 directions.
Restore the cell after recursion (backtracking).
If any path succeeds, return True; otherwise False.

Time Complexity:
O(n * m * 4^L) where L = length of word
Space Complexity:
O(L) recursion stack   
'''

class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        def dfs(i, j, k):
            # All characters matched
            if k == len(word):
                return True
            
            # Boundary and mismatch checks
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[k]:
                return False
            
            # Mark as visited
            temp = mat[i][j]
            mat[i][j] = '#'
            
            # Explore 4 directions
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))
            
            # Backtrack
            mat[i][j] = temp
            
            return found
        
        # Try starting from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
