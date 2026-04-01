#Problem Name: Max Circular Subarray Sum

# Intuition
'''
In a circular array, the maximum subarray sum can come from two possible cases:

1) Non-wrapping subarray:
   This is the classic maximum subarray problem, which can be solved using Kadane’s algorithm.

2) Wrapping subarray:
   Here, the subarray wraps around the end to the beginning of the array.
   This can be thought of as:
   total_sum_of_array - minimum_subarray_sum

So, the final answer is the maximum of:
- maximum subarray sum (non-wrapping)
- total sum - minimum subarray sum (wrapping)

Edge case:
If all elements are negative, the wrapping case becomes invalid (it would give 0),
so we simply return the maximum element (Kadane’s result).
'''

# Approach
'''
1) Use Kadane’s algorithm to find:
   - max_kadane: maximum subarray sum (non-wrapping case)
   - min_kadane: minimum subarray sum

2) Compute total_sum of the array.

3) If max_kadane is negative:
   - All elements are negative, return max_kadane.

4) Otherwise:
   - wrapping_sum = total_sum - min_kadane
   - return max(max_kadane, wrapping_sum)
'''

class Solution:
    def maxCircularSum(self, arr):
        # Step 1: Initialize variables
        total_sum = 0
        
        max_ending = max_so_far = arr[0]
        min_ending = min_so_far = arr[0]
        
        # Step 2: Traverse the array
        for i in range(len(arr)):
            total_sum += arr[i]
            
            if i > 0:
                max_ending = max(arr[i], max_ending + arr[i])
                max_so_far = max(max_so_far, max_ending)
                
                min_ending = min(arr[i], min_ending + arr[i])
                min_so_far = min(min_so_far, min_ending)
        
        # Step 3: Handle all-negative case
        if max_so_far < 0:
            return max_so_far
        
        # Step 4: Return the maximum of wrapping and non-wrapping cases
        return max(max_so_far, total_sum - min_so_far)
