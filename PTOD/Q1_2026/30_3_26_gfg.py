'''
INTUITION:
This problem is essentially asking us to connect all given points (houses)
such that the total cost is minimized, where cost is defined as Manhattan distance.

This is a classic Minimum Spanning Tree (MST) problem:
- Each house is a node.
- Cost between any two houses is the edge weight.
- We need to connect all nodes with minimum total edge weight.

APPROACH:
We can solve this using Prim’s Algorithm (greedy MST approach):

Steps:
1. Start with any node (say index 0).
2. Maintain a visited array to track nodes already included in MST.
3. Keep a min distance array where minDist[i] stores the minimum cost
    to connect node i to the MST.
4. Initially, minDist[0] = 0 and rest are infinity.
5. Repeat n times:
    a. Pick the unvisited node with minimum minDist.
    b. Add its cost to result.
    c. Mark it as visited.
    d. Update distances of all unvisited nodes using Manhattan distance.
6. The total accumulated cost is the answer.

Time Complexity: O(n^2)
Space Complexity: O(n)
'''
class Solution:
    def minCost(self, houses):

        n = len(houses)
        visited = [False] * n
        minDist = [float('inf')] * n
        
        minDist[0] = 0
        total_cost = 0

        for _ in range(n):
            # Pick the minimum distance unvisited node
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i

            # Add its cost
            total_cost += minDist[u]
            visited[u] = True

            # Update distances of remaining nodes
            for v in range(n):
                if not visited[v]:
                    cost = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if cost < minDist[v]:
                        minDist[v] = cost

        return total_cost