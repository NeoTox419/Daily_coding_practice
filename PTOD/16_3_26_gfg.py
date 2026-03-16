#Problem Name: K Sum Paths
'''
Intuition
---------
We need to count all paths in a binary tree whose sum equals k.  
The path must go downward (parent → child), but it can start from any node and end at any node.

A naive idea would be:
For every node, start a DFS and check all downward paths starting from that node.  
However, that would lead to O(N^2) in the worst case.

Instead, we use the **Prefix Sum technique** (similar to subarray sum equals k).

Key Idea:
If the current prefix sum from root to current node is `curr_sum`,
and there was a previous prefix sum `curr_sum - k`,
then the nodes between them form a path whose sum is `k`.

So we store how many times each prefix sum has appeared while traversing the tree.

Example:
If current sum = 15 and k = 8  
We check if (15 - 8 = 7) appeared before.  
If yes, that means a path summing to 8 exists ending at this node.

Approach
--------
1. Use DFS traversal.
2. Maintain a running prefix sum.
3. Use a hashmap (dictionary) to store frequency of prefix sums.
4. At each node:
   - Add node value to current sum.
   - Check if (curr_sum - k) exists in hashmap → add its frequency to answer.
5. Add curr_sum to hashmap before exploring children.
6. After finishing children, decrement its frequency (backtracking).
7. Return total count.

Time Complexity: O(N)  
Space Complexity: O(N) (recursion + hashmap)
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def countAllPaths(self, root, k):
        
        prefix = {0: 1}  # base case: prefix sum 0 occurs once
        count = 0
        
        def dfs(node, curr_sum):
            nonlocal count
            
            if not node:
                return
            
            # update current prefix sum
            curr_sum += node.data
            
            # check if there exists a prefix sum such that
            # curr_sum - prefix_sum = k
            count += prefix.get(curr_sum - k, 0)
            
            # add current prefix sum to hashmap
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            # traverse children
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # backtrack
            prefix[curr_sum] -= 1
        
        dfs(root, 0)
        return count