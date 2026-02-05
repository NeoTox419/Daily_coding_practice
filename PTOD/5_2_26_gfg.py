#Problem Name: Maximize Number of 1's
"""0
    Intuition:
    ----------
    We want the longest subarray that contains at most `k` zeros,
    because we are allowed to flip at most `k` zeros into ones.
    If a window has <= k zeros, it can be converted into all 1s.

    So the problem becomes:
    👉 Find the longest contiguous subarray with at most k zeros.

    ------------------------------------------------------------

    Approach (Sliding Window):
    ---------------------------
    1. Use two pointers: `left` and `right` to maintain a window.
    2. Expand `right` to include new elements.
    3. If the element at `right` is 0, increment zero_count.
    4. If zero_count exceeds k:
        - Shrink the window from the left
        - Decrease zero_count when a 0 is removed
    5. At every step, calculate the window size and update max length.

    This works because:
    - Each element is processed at most twice
    - Time Complexity is O(n)
    - Space Complexity is O(1)

    ------------------------------------------------------------
"""

class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1

            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
