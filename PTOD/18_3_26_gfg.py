#Problem name: Distribute Candies
'''
Intuition:
Each node should have exactly one candy.
If a node has extra candies, it passes them to its parent/child.
If it has fewer candies, it receives from neighbors.
We calculate surplus/deficit using post-order traversal.

Approach:
1. Traverse tree in post-order.
2. For each node:
    - Get left and right subtree balances.
    - Add abs(left_balance) + abs(right_balance) to moves.
    - Return current balance:
        node.data + left_balance + right_balance - 1
3. Final moves give minimum operations required.
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def distCandy(self, root):
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # moves required to balance left and right subtree
            self.moves += abs(left) + abs(right)

            # return balance to parent
            return node.data + left + right - 1

        dfs(root)
        return self.moves