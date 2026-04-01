#problem name:K Sized Subarray Maximum
'''
Given an array arr[] of positive integers and an integer k.You have to find the maximum value for each contiguous subarray of size k.
Return an array of maximum values corresponding to each contiguous subarray.
'''

from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):
            if dq and dq[0] == i - k:
                dq.popleft()

            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
