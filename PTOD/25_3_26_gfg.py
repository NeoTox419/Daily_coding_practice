#porblem name:Minimum height roots

'''
A tree has no cycles and is connected.

If we root the tree at different nodes, the height changes.
We want nodes that minimize the maximum distance to any other node.

Key idea:
The root that gives minimum height lies near the "center" of the tree.

Think of the tree like a long chain:
The best root is the middle node (or two middle nodes).

So instead of trying every node (costly),
we REMOVE LEAVES layer by layer (like peeling an onion).

Eventually, we are left with 1 or 2 nodes:
→ These are the centroids
→ These give minimum height trees
'''

'''
1. Build adjacency list for the graph.
2. Compute degree of each node.

3. Push all leaf nodes (degree == 1) into a queue.

4. Remove leaves level by level:
   - Reduce degree of neighbors
   - If neighbor becomes leaf → push to queue

5. Keep removing until <= 2 nodes remain.

6. Remaining nodes are the answer.
'''

from collections import defaultdict, deque

class Solution:
    def minHeightRoot(self, V, edges):
        # Edge case
        if V == 1:
            return [0]

        # Step 1: Build graph
        graph = defaultdict(list)
        degree = [0] * V

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Step 2: Initialize leaves
        q = deque()
        for i in range(V):
            if degree[i] == 1:
                q.append(i)

        remaining_nodes = V

        # Step 3: Trim leaves
        while remaining_nodes > 2:
            size = len(q)
            remaining_nodes -= size

            for _ in range(size):
                leaf = q.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        q.append(neighbor)

        # Step 4: Remaining nodes are centroids
        return list(q)