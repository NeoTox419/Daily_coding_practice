"""
    Problem Name: Sum of Subarray Ranges
    ===================== INTUITION =====================

    For any subarray:
        range = max(subarray) - min(subarray)

    If we sum this over all subarrays, we can rearrange it as:
        sum_of_all_maximums - sum_of_all_minimums

    So the problem reduces to:
        1) Find sum of maximum elements over all subarrays
        2) Find sum of minimum elements over all subarrays
        3) Subtract (1) - (2)

    -----------------------------------------------------

    ===================== KEY OBSERVATION =====================

    Consider a fixed element arr[i].

    Instead of iterating over all subarrays, we count:
        - In how many subarrays is arr[i] the maximum?
        - In how many subarrays is arr[i] the minimum?

    If:
        left = number of choices to extend subarray to the left
        right = number of choices to extend subarray to the right

    Then:
        total subarrays where arr[i] is the max/min = left * right

    Contribution of arr[i]:
        arr[i] * left * right

    -----------------------------------------------------

    ===================== HOW TO FIND left & right =====================

    We use MONOTONIC STACKS.

    For MAX contribution:
        - Previous Greater Element (strictly greater)
        - Next Greater or Equal Element

    For MIN contribution:
        - Previous Smaller Element (strictly smaller)
        - Next Smaller or Equal Element

    This choice avoids double-counting duplicates.

    -----------------------------------------------------

    ===================== FINAL FORMULA =====================

    answer = (sum of max contributions) - (sum of min contributions)

    Time Complexity: O(n)
    Space Complexity: O(n)

    ========================================================
"""
class Solution:
    def subarrayRanges(self, arr):

        n = len(arr)

        # Helper function to compute total contribution
        # If is_max = True  -> calculates sum of maximums
        # If is_max = False -> calculates sum of minimums
        def get_contribution(is_max):
            stack = []
            left = [0] * n
            right = [0] * n

            # ---------- LEFT SIDE ----------
            # Count how far we can extend to the left
            for i in range(n):
                # Maintain monotonic stack
                while stack and (
                    arr[stack[-1]] < arr[i] if is_max else arr[stack[-1]] > arr[i]
                ):
                    stack.pop()

                # Distance to previous greater/smaller
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack.clear()

            # ---------- RIGHT SIDE ----------
            # Count how far we can extend to the right
            for i in range(n - 1, -1, -1):
                while stack and (
                    arr[stack[-1]] <= arr[i] if is_max else arr[stack[-1]] >= arr[i]
                ):
                    stack.pop()

                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            # ---------- TOTAL CONTRIBUTION ----------
            total = 0
            for i in range(n):
                total += arr[i] * left[i] * right[i]

            return total

        # Sum of maximums of all subarrays
        max_sum = get_contribution(is_max=True)

        # Sum of minimums of all subarrays
        min_sum = get_contribution(is_max=False)

        # Final answer
        return max_sum - min_sum
