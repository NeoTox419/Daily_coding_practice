class Solution:
    def largestBst(self, root):
        '''
        INTUITION:
        ----------
        A Binary Search Tree (BST) must satisfy:
        - Left subtree values < root
        - Right subtree values > root
        - Both left and right subtrees must also be BSTs
        
        Instead of checking every subtree separately (which would be slow),
        we use a bottom-up approach (postorder traversal).
        
        At each node, we try to determine:
        - Is the subtree rooted at this node a BST?
        - If yes → what is its size?
        - If not → propagate the largest BST size found so far.
        
        
        APPROACH:
        ---------
        For each node, return 3 values:
        1. size  → size of the largest BST in this subtree
        2. min   → minimum value in this subtree
        3. max   → maximum value in this subtree
        
        Base case:
        - For null node:
            size = 0
            min = +inf
            max = -inf
        
        For each node:
        - Recursively get info from left and right
        
        If:
            left.max < root.data < right.min
        → Then current subtree is a BST:
            size = left.size + right.size + 1
            min = min(root.data, left.min)
            max = max(root.data, right.max)
        
        Else:
        → Not a BST:
            size = max(left.size, right.size)
            Return invalid range (min = -inf, max = +inf)
            so parent cannot treat this as BST
        
        Finally:
        - The answer is stored in size returned for root
        
        Time Complexity: O(N)
        Space Complexity: O(H) recursion stack
        '''
        
        def helper(node):
            if not node:
                return (0, float('inf'), float('-inf'))
            
            left_size, left_min, left_max = helper(node.left)
            right_size, right_min, right_max = helper(node.right)
            
            # Check if current subtree is BST
            if left_max < node.data < right_min:
                size = left_size + right_size + 1
                min_val = min(node.data, left_min)
                max_val = max(node.data, right_max)
                return (size, min_val, max_val)
            
            # Not a BST
            return (max(left_size, right_size), float('-inf'), float('inf'))
        
        return helper(root)[0]