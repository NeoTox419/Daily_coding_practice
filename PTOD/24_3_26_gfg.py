#Porblem Name: Course Schedule I
'''
INTUITION:
This problem is about detecting whether a cycle exists in a directed graph.
Each course is a node, and a prerequisite [x, y] means an edge from y → x.
If there is a cycle, it means we cannot complete all courses because
some courses depend on each other circularly.

APPROACH (Kahn’s Algorithm - Topological Sort using BFS):
1. Build a graph (adjacency list) from prerequisites.
2. Maintain an indegree array where indegree[i] = number of prerequisites for course i.
3. Add all nodes with indegree 0 (no prerequisites) to a queue.
4. Process nodes from the queue:
    - Remove a node and count it as completed.
    - For all its neighbors, reduce their indegree by 1.
    - If any neighbor's indegree becomes 0, add it to the queue.
5. If we are able to process all n nodes, return True.
    Otherwise, a cycle exists → return False.
'''
class Solution:
    def canFinish(self, n, prerequisites):
        from collections import deque

        # Step 1: Build graph and indegree array
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for x, y in prerequisites:
            graph[y].append(x)  # y → x
            indegree[x] += 1

        # Step 2: Initialize queue with nodes having indegree 0
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process nodes
        count = 0  # number of courses completed

        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are completed
        return count == n