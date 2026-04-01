'''
INTUITION:
-----------
When it rains, water gets trapped between taller blocks.
For any block at index i, the amount of water it can hold depends on:

    1. The tallest block to its left
    2. The tallest block to its right

Because water can only rise up to the minimum of those two heights.

So at index i:
    Water trapped = min(max_left, max_right) - height[i]

If this value is negative, we treat it as 0.

The key idea:
Water above a block is determined by the shorter boundary
between the tallest block on the left and right.


APPROACH:
-----------
We use the TWO POINTER technique to optimize space.

1. Initialize two pointers:
       left = 0
       right = n - 1

2. Keep track of:
       left_max  -> maximum height from left
       right_max -> maximum height from right

3. Move pointers inward:
   - If arr[left] < arr[right]:
         If arr[left] >= left_max:
               update left_max
         Else:
               water += left_max - arr[left]
         Move left pointer forward

   - Else:
         If arr[right] >= right_max:
               update right_max
         Else:
               water += right_max - arr[right]
         Move right pointer backward

Why this works:
Water trapped depends on the smaller boundary.
By comparing heights at both ends, we safely decide
which side to process.

Time Complexity: O(n)
Space Complexity: O(1)
'''


class Solution:
    def maxWater(self, arr):
        n = len(arr)
        
        if n == 0:
            return 0
        
        left = 0
        right = n - 1
        
        left_max = 0
        right_max = 0
        
        water = 0
        
        while left <= right:
            
            if arr[left] <= arr[right]:
                
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                
                left += 1
            
            else:
                
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                
                right -= 1
        
        return water