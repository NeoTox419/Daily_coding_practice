'''
INTUITION:
We need to maximize the minimum height among all flowers after k days.
Each day, we can choose w consecutive flowers and increase their height by 1.

Instead of directly simulating watering, we think in reverse:
Suppose we want every flower to have at least height = X.
Can we achieve this using at most k watering operations?

If we can check whether a target minimum height X is achievable,
then we can apply Binary Search on the answer.

Key idea:
- The minimum height after watering lies between min(arr) and min(arr) + k.
- For a candidate height X, we greedily ensure every flower reaches X.
- When a flower at position i is below X, we must water starting at i
    (covering i to i+w-1) to raise it.
- Use a difference-array (prefix increment technique) to efficiently
    simulate range increments in O(n).


APPROACH:
1. Binary search the answer between:
    low = min(arr)
    high = min(arr) + k
    
2. For each mid (candidate minimum height):
    - Traverse flowers from left to right.
    - Maintain:
        * current increment effect using prefix sum technique
        * difference array to simulate range updates
    - If arr[i] + current_increment < mid:
        -> We need extra = mid - current_height
        -> Perform watering starting at i
        -> Increase total operations used
        -> If total operations > k, return False
        
3. If feasible, move right (try bigger minimum).
    Else move left.
    
Time Complexity:
    O(n log k)
Space Complexity:
    O(n)
'''
class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        def canAchieve(target):
            diff = [0] * (n + 1)
            current = 0
            operations = 0
            
            for i in range(n):
                current += diff[i]
                
                if arr[i] + current < target:
                    need = target - (arr[i] + current)
                    operations += need
                    
                    if operations > k:
                        return False
                    
                    current += need
                    if i + w <= n:
                        diff[i + w] -= need
                        
            return True
        
        low = min(arr)
        high = min(arr) + k
        answer = low
        
        while low <= high:
            mid = (low + high) // 2
            
            if canAchieve(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return answer
