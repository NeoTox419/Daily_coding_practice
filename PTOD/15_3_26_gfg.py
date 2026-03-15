'''
Intuition
---------
In vertical traversal, we group nodes that lie on the same vertical line when the tree is viewed from top.

We can imagine assigning a horizontal distance (HD) to each node:
- Root has HD = 0
- Left child has HD = parent_HD - 1
- Right child has HD = parent_HD + 1

Nodes with the same HD belong to the same vertical column.

The problem also requires that if multiple nodes fall on the same vertical line,
they must appear in level order. Because of this, we use Breadth First Search (BFS)
instead of DFS. BFS naturally processes nodes level by level.

Approach
--------
1. If the root is None, return an empty list.

2. Use a queue for BFS traversal. Each element in the queue stores:
      (node, horizontal_distance)

3. Maintain a dictionary (or defaultdict list) to store nodes for each HD.

4. Start BFS from the root with HD = 0.

5. For every node popped from the queue:
      - Append its value to the list corresponding to its HD.
      - If left child exists → push (left_child, HD - 1)
      - If right child exists → push (right_child, HD + 1)

6. Track the minimum and maximum HD encountered.

7. Finally, traverse HD from min_HD to max_HD and append stored node values
   in order to the result list.

Time Complexity
---------------
O(N) because each node is visited once.

Space Complexity
----------------
O(N) for the queue and hashmap storing vertical columns.
'''

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
        
        # Dictionary to store nodes for each horizontal distance
        column_table = defaultdict(list)
        
        # Queue for BFS -> (node, horizontal_distance)
        q = deque([(root, 0)])
        
        min_hd = max_hd = 0
        
        while q:
            node, hd = q.popleft()
            
            column_table[hd].append(node.data)
            
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        
        for hd in range(min_hd, max_hd + 1):
            result.extend(column_table[hd])
        
        return result