#Problem name: Count increasing Subaarays
'''
We need to count all subarrays that are:
1. Contiguous
2. Strictly increasing
3. Length >= 2

Instead of checking all subarrays (which would be O(n^2)), 
we can observe a pattern:

If we find a continuous increasing segment, say:
[1, 2, 3, 4]

Then all its increasing subarrays are:
[1,2], [2,3], [3,4], [1,2,3], [2,3,4], [1,2,3,4]

If the length of such segment is L,
number of valid subarrays = L * (L - 1) / 2

So the problem reduces to:
→ Find lengths of all strictly increasing contiguous segments
→ Sum their contributions
'''

'''
1. Traverse the array once.
2. Maintain a variable `length` = current increasing segment length.
3. If arr[i] > arr[i-1]:
      increase length
   Else:
      compute contribution of previous segment
      reset length = 1
4. After loop, add contribution of last segment.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def countIncreasing(self, arr):        
        n = len(arr)
        if n < 2:
            return 0
        
        count = 0
        length = 1  # current increasing segment length
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                if length >= 2:
                    count += (length * (length - 1)) // 2
                length = 1
        
        # handle last segment
        if length >= 2:
            count += (length * (length - 1)) // 2
        
        return count