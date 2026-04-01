#problem name: Longest subarray with Atmost two distinct integers
'''
Intuition:
-----------
We need to find the longest contiguous subarray that contains
at most two distinct integers. This is a classic "sliding window"
problem.

Since we are allowed at most two distinct integers, we can:
- Expand the window to the right while the condition is valid.
- If adding a new element causes more than two distinct integers,
    we shrink the window from the left until we are back to
    at most two distinct integers.

Approach:
----------
1. Use two pointers (left and right) to represent the sliding window.
2. Use a dictionary (hash map) to store the frequency of elements
    in the current window.
3. Move the right pointer forward and update frequency.
4. If the number of distinct elements exceeds 2:
        - Move the left pointer forward
        - Decrease frequency
        - Remove elements whose frequency becomes 0
5. At every valid window (with <= 2 distinct elements),
    calculate the window length and update the maximum length.
6. Return the maximum length found.

Time Complexity: O(N)
Space Complexity: O(1)  (at most 3 keys in dictionary)
'''
class Solution:
    def totalElements(self, arr):
        left = 0
        max_length = 0
        freq = {}

        for right in range(len(arr)):
            # Add current element to frequency map
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            # If more than 2 distinct elements, shrink window
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length