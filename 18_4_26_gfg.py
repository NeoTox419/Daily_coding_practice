'''
Intuition:
Flipping a subarray converts 0 → 1 (gain +1) and 1 → 0 (loss -1).
So we transform the problem into finding a subarray that gives maximum net gain.

Approach:
1. Count total number of 1s in the original array.
2. Transform array:
    - Replace 0 with +1 (gain)
    - Replace 1 with -1 (loss)
3. Use Kadane's Algorithm to find maximum subarray sum.
4. Result = total_ones + max_gain
5. If max_gain is negative, don't flip → return total_ones.
'''
class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)

        max_gain = 0
        curr_gain = 0

        for num in arr:
            value = 1 if num == 0 else -1
            curr_gain = max(value, curr_gain + value)
            max_gain = max(max_gain, curr_gain)

        return total_ones + max_gain