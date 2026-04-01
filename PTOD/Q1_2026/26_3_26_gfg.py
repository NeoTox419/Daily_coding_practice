'''
Intuition:
- We need shortest time from node 0 to node V-1.
- Along with shortest distance, we also count number of ways.
- Use Dijkstra’s Algorithm.
- Maintain:
    dist[i] = shortest distance to node i
    ways[i] = number of shortest paths to node i

Approach:
- Build adjacency list.
- Initialize:
    dist[0] = 0, ways[0] = 1
- Use min heap (distance, node).
- For each neighbor:
    If new_dist < dist[neighbor]:
        update dist
        ways[neighbor] = ways[current]
    If new_dist == dist[neighbor]:
        ways[neighbor] += ways[current]
- Return ways[V-1]
'''
import heapq

class Solution:
    def countPaths(self, V, edges):

        MOD = 10**9 + 7

        # Step 1: Build graph
        graph = [[] for _ in range(V)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Step 2: Initialize distance and ways
        dist = [float('inf')] * V
        ways = [0] * V

        dist[0] = 0
        ways[0] = 1

        # Step 3: Min heap (distance, node)
        heap = [(0, 0)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            # Skip outdated entries
            if curr_dist > dist[node]:
                continue

            for neighbor, time in graph[node]:
                new_dist = curr_dist + time

                # Found shorter path
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_dist, neighbor))

                # Found another shortest path
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[V - 1]