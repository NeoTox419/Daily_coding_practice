#Problem Name: Rotting Oranges
'''
INTUITION:
This problem is essentially a "multi-source BFS" problem.

- All rotten oranges (value = 2) act as starting points.
- In each unit time, they spread rot to adjacent fresh oranges (value = 1).
- This spreading happens level by level (like BFS layers).

Think of it like fire spreading in waves:
- At time = 0 → all initially rotten oranges
- At time = 1 → oranges adjacent to them rot
- At time = 2 → next layer rots
... and so on.

So, the minimum time required is the number of BFS levels needed
to rot all fresh oranges.

If some fresh oranges are unreachable, return -1.
'''

'''
APPROACH:
1. Traverse the matrix:
    - Add all rotten oranges (2) to a queue with time = 0
    - Count total fresh oranges

2. Perform BFS:
    - For each rotten orange, try to rot its 4-directional neighbors
    - If a fresh orange is found:
        → mark it rotten
        → decrease fresh count
        → push it into queue with time + 1

3. Track the maximum time encountered during BFS

4. After BFS:
    - If fresh oranges still remain → return -1
    - Else → return time taken
'''
class Solution:
    def orangesRot(self, mat):

        from collections import deque

        if not mat or not mat[0]:
            return 0

        rows, cols = len(mat), len(mat[0])
        q = deque()
        fresh = 0

        # Step 1: Initialize queue and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    q.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh += 1

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        time = 0

        # Step 2: BFS
        while q:
            i, j, t = q.popleft()
            time = max(time, t)

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] == 1:
                    mat[ni][nj] = 2   # rot it
                    fresh -= 1
                    q.append((ni, nj, t + 1))

        # Step 3: Check if any fresh orange remains
        return -1 if fresh > 0 else time