#Problem Name: Find Kth Rotation
'''
-----------------------------------------------
Intuition:
-----------------------------------------------
A sorted increasing array, when right-rotated k times,
will have its smallest element shifted from index 0
to index k.

Example:
Original sorted array: [2, 4, 6, 9]
Right rotated 2 times: [6, 9, 2, 4]

Notice:
- The array is still "almost sorted"
- The minimum element (2) tells us how many rotations happened
- Index of the minimum element == number of right rotations (k)

So the task reduces to:
-> Find the index of the minimum element efficiently


-----------------------------------------------
Approach:
-----------------------------------------------
Since the array was originally sorted and then rotated,
we can use Binary Search to find the minimum element
in O(log n) time.

Steps:
1. Use binary search with low = 0, high = n - 1
2. If arr[mid] > arr[high]:
      - Minimum lies in the right half
3. Else:
      - Minimum lies in the left half (including mid)
4. Continue until low == high

The final index 'low' will point to the smallest element,
which is also the number of right rotations (k).
'''
class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[high]:
                # Minimum is in the right half
                low = mid + 1
            else:
                # Minimum is in the left half (or at mid)
                high = mid

        # 'low' is the index of the minimum element
        return low