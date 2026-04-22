#Problem name: Mean of range in array
'''
Intuition:
A brute-force approach would compute the sum for each query range [l, r]
by iterating over the subarray every time. This would take O(n) per query,
leading to O(n * q) overall complexity, which is inefficient for large inputs.

To optimize, we observe that we are repeatedly calculating sums of subarrays.
This is a classic use case for prefix sum.

Approach:
1. Build a prefix sum array where:
    prefix[i] = sum of elements from index 0 to i-1
    (we use size n+1 for convenience)

2. Using prefix sum, sum of subarray [l, r] can be computed as:
    subarray_sum = prefix[r+1] - prefix[l]

3. Compute mean:
    mean = subarray_sum // (r - l + 1)
    (floor division ensures we return the floor value)

4. Do this for all queries and store results.

Time Complexity:
- Prefix computation: O(n)
- Each query: O(1)
- Total: O(n + q)

Space Complexity:
- O(n) for prefix array
'''
class Solution:
    def findMean(self, arr, queries):
        n = len(arr)

        # Step 1: Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        result = []

        # Step 2: Process queries
        for l, r in queries:
            sub_sum = prefix[r + 1] - prefix[l]
            length = r - l + 1
            mean = sub_sum // length  # floor value
            result.append(mean)

        return result