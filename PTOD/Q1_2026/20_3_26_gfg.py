#problem name: predecessor and successor
'''
INTUITION:
----------
In a Binary Search Tree (BST), for any node:
- Left subtree contains smaller values
- Right subtree contains greater values

So:
- Predecessor = largest value smaller than key
- Successor   = smallest value greater than key

We can exploit BST properties to avoid full traversal.


APPROACH:
----------
1. Initialize:
    pre = None, suc = None

2. Traverse the tree:

Case 1: root.data == key
    - Predecessor:
        Go to left subtree → keep moving right to get max
    - Successor:
        Go to right subtree → keep moving left to get min

Case 2: key < root.data
    - Current node can be a successor
    - Store it and move LEFT

Case 3: key > root.data
    - Current node can be a predecessor
    - Store it and move RIGHT

3. Continue until root becomes None

Time Complexity: O(h) where h = height of tree
Space Complexity: O(1)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None

        while root:
            if root.data == key:
                # Find predecessor (max in left subtree)
                if root.left:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    pre = temp

                # Find successor (min in right subtree)
                if root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    suc = temp

                break

            elif key < root.data:
                suc = root
                root = root.left

            else:
                pre = root
                root = root.right

        return pre, suc