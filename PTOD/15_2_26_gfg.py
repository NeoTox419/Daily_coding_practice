'''
INTUITION:
-----------
This is a classic "Painter's Partition Problem".

Each painter can only paint a contiguous sequence of boards.
We must divide the array into at most k contiguous partitions
such that the maximum workload among painters is minimized.

Key Observations:
- Minimum possible time = max(arr)
    (because one painter must at least paint the largest board)
- Maximum possible time = sum(arr)
    (if only one painter paints everything)

So the answer lies between:
    low = max(arr)
    high = sum(arr)

We can use Binary Search on the answer (time).
'''

'''
APPROACH:
----------
1. Use Binary Search between low = max(arr) and high = sum(arr).
2. For a mid value (candidate time), check if we can paint all boards
    using <= k painters such that no painter paints more than mid length.
3. To check feasibility:
    - Start assigning boards to the current painter.
    - If adding a board exceeds mid, assign a new painter.
    - Count how many painters are needed.
4. If painters_needed <= k:
        It is possible → try smaller time (high = mid - 1)
    Else:
        Not possible → increase time (low = mid + 1)
5. Return the minimum valid time found.
'''

class Solution:
    def minTime(self, arr, k):
        def is_possible(max_time):
            painters = 1
            current_sum = 0

            for length in arr:
                if current_sum + length <= max_time:
                    current_sum += length
                else:
                    painters += 1
                    current_sum = length
                    if painters > k:
                        return False
            return True

        low = max(arr)
        high = sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2

            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
