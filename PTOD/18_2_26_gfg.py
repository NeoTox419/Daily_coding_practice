"""
INTUITION:
----------
An inversion is a pair (i, j) such that:
    i < j and arr[i] > arr[j]

A simple idea is:
    - For every element, compare it with elements to its right.
    - Count whenever arr[i] > arr[j].

But this takes O(n^2) time, which is too slow for large arrays.

Key Observation:
If we use a modified Merge Sort:
    - During merging of two sorted halves,
    - If left[i] > right[j], then
        all remaining elements in left (from i onward)
        will also form inversions with right[j].

This helps count inversions efficiently in O(n log n).


APPROACH:
----------
1. Use Merge Sort algorithm.
2. Divide the array into two halves.
3. Recursively count inversions in:
        - Left half
        - Right half
4. While merging:
        - If left[i] <= right[j] → no inversion.
        - If left[i] > right[j] → 
            inversion_count += (mid - i + 1)
        because all remaining elements in left
        are greater than right[j].
5. Return total inversions.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
class Solution:
    def inversionCount(self, arr):

        def merge_sort(arr, left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            inv_count = 0

            # Count inversions in left half
            inv_count += merge_sort(arr, left, mid)

            # Count inversions in right half
            inv_count += merge_sort(arr, mid + 1, right)

            # Count cross inversions while merging
            inv_count += merge(arr, left, mid, right)

            return inv_count

        def merge(arr, left, mid, right):
            temp = []
            i = left
            j = mid + 1
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv_count += (mid - i + 1)
                    j += 1

            # Remaining elements
            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            # Copy back to original array
            for k in range(len(temp)):
                arr[left + k] = temp[k]

            return inv_count

        return merge_sort(arr, 0, len(arr) - 1)
