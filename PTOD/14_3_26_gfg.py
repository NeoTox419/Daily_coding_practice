#Porblem name: Top view of Binary Tree
'''
Intuition:
The top view of a binary tree consists of the nodes that are visible
when the tree is observed from the top. If we assign a horizontal
distance (HD) to every node relative to the root, we can determine
which node appears first at each horizontal position.

- Root has horizontal distance (HD) = 0
- Left child → HD - 1
- Right child → HD + 1

For each horizontal distance, the first node encountered (closest to
the root) should be included in the top view.

Approach:
1. Use Breadth First Search (BFS) because it processes nodes level by level,
    ensuring that the first node encountered for a horizontal distance
    is the topmost one.
2. Maintain a queue storing tuples: (node, horizontal_distance).
3. Maintain a dictionary (or map) to store the first node seen at each HD.
4. Traverse the tree:
    - If an HD is not already in the map, store the node value.
    - Push left child with HD-1 and right child with HD+1 into the queue.
5. After traversal, sort the dictionary keys (HDs).
6. Return the node values from the smallest HD to the largest HD.
'''
class Solution:
    def topView(self, root):
        if not root:
            return []

        from collections import deque

        q = deque([(root, 0)])
        top_nodes = {}

        while q:
            node, hd = q.popleft()

            if hd not in top_nodes:
                top_nodes[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        result = []
        for hd in sorted(top_nodes):
            result.append(top_nodes[hd])

        return result