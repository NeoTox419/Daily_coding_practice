#Problem name: check if subtree
# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Solution:
    """
    Intuition:
    ----------
    We need to check whether tree S (root2) exists inside tree T (root1)
    as an exact subtree.

    Main idea:
    1. Traverse every node of tree T.
    2. Whenever we find a node in T whose value matches the root of S,
       check whether both trees are IDENTICAL from that point.
    3. If identical -> return True.
    4. Otherwise continue searching.

    Two trees are identical if:
    - Their node values are equal
    - Left subtrees are identical
    - Right subtrees are identical

    Time Complexity:
    ----------------
    Worst Case: O(N * M)
    where:
    N = number of nodes in T
    M = number of nodes in S

    Space Complexity:
    -----------------
    O(H)
    H = height of recursion stack
    """

    def isSubTree(self, root1, root2):

        # Helper function to check if two trees are identical
        def isIdentical(a, b):

            # Both nodes are null
            if not a and not b:
                return True

            # One is null and the other is not
            if not a or not b:
                return False

            # Current node values must match
            if a.data != b.data:
                return False

            # Recursively check left and right subtrees
            return (isIdentical(a.left, b.left) and
                    isIdentical(a.right, b.right))

        # Empty tree S is always a subtree
        if not root2:
            return True

        # If T becomes empty but S still exists
        if not root1:
            return False

        # If trees match from current node
        if isIdentical(root1, root2):
            return True

        # Otherwise search in left or right subtree
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))