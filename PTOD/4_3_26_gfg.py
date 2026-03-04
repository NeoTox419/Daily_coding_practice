'''
Intuition:
A subarray of size k means we only consider contiguous segments of length k.
For each such subarray, we need to compute the XOR of its elements and keep
track of the maximum XOR obtained.

Brute Force Idea:
For every starting index i from 0 to n-k:
compute XOR of elements from i to i+k-1
update maximum if needed
This would take O(n*k) time.

Optimization (Sliding Window with XOR):
XOR has a useful property:
a ^ b ^ b = a

If we know the XOR of the current window of size k:
window_xor = arr[i] ^ arr[i+1] ^ ... ^ arr[i+k-1]

When we slide the window by one position:
remove arr[i] and add arr[i+k]

New XOR becomes:
window_xor = window_xor ^ arr[i] ^ arr[i+k]

This allows computing each window XOR in O(1) time after the first window.

Steps:
1. Compute XOR of the first k elements.
2. Store it as the current maximum.
3. Slide the window across the array updating XOR each time.
4. Update maximum XOR whenever a larger value is found.

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:

    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        # XOR of first window
        window_xor = 0
        for i in range(k):
            window_xor ^= arr[i]

        max_xor = window_xor

        # Slide the window
        for i in range(k, n):
            window_xor ^= arr[i-k]  # remove outgoing element
            window_xor ^= arr[i]    # add incoming element
            max_xor = max(max_xor, window_xor)

        return max_xor