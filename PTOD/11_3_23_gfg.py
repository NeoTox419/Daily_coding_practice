class Solution:
    def sumSubMins(self, arr):
        '''
        INTUITION
        ---------
        If we try the brute force approach, we would generate all possible
        subarrays and compute the minimum of each. Since the number of
        subarrays is O(n^2), this becomes too slow for large inputs.

        Instead, think in terms of contribution of each element.

        For an element arr[i], we determine how many subarrays exist
        where arr[i] is the minimum element.

        If we find:
        - Previous Less Element index (PLE)
        - Next Less Element index (NLE)

        Then the number of subarrays where arr[i] is the minimum is:

            (i - PLE) * (NLE - i)

        Because:
        - (i - PLE) choices exist for the left boundary
        - (NLE - i) choices exist for the right boundary

        Contribution of arr[i] to the final sum is:

            arr[i] * (i - PLE) * (NLE - i)


        APPROACH
        --------
        1. Use a monotonic increasing stack to find Previous Less Element (PLE).
        2. Use another pass to find Next Less Element (NLE).
        3. For each element calculate:
                contribution = arr[i] * left_count * right_count
        4. Sum all contributions.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        n = len(arr)
        ple = [0] * n
        nle = [0] * n
        stack = []

        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Less Element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            nle[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            ans += arr[i] * left * right

        return ans