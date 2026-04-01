#problem name:Pythagorean Triplet
'''
Intuition:
A Pythagorean triplet satisfies the condition:
a^2 + b^2 = c^2

Instead of checking every combination directly (which would take O(n^3)),
we can simplify the problem by squaring all elements first. Then the
condition becomes:

arr[i] + arr[j] = arr[k]

If we sort the squared values, we can treat arr[k] as the largest element
(c^2) and try to find two numbers before it whose sum equals it.

This is similar to the classic "two-sum in a sorted array" problem.

Approach:
1. Square all elements of the array.
2. Sort the squared array.
3. Fix the largest value as c^2 (iterate from end to start).
4. Use two pointers:
   - left at the beginning
   - right just before c
5. If arr[left] + arr[right] == arr[c], we found a Pythagorean triplet.
6. If the sum is smaller, move left pointer forward.
7. If the sum is larger, move right pointer backward.
8. If no such combination is found, return False.

Time Complexity: O(n^2)
Space Complexity: O(1) (ignoring input modification)
'''

class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        
        # Step 1: Square all elements
        for i in range(n):
            arr[i] = arr[i] * arr[i]
        
        # Step 2: Sort the array
        arr.sort()
        
        # Step 3: Fix c^2 from the end
        for c in range(n - 1, 1, -1):
            left = 0
            right = c - 1
            
            # Step 4: Two pointer search
            while left < right:
                if arr[left] + arr[right] == arr[c]:
                    return True
                elif arr[left] + arr[right] < arr[c]:
                    left += 1
                else:
                    right -= 1
        
        return False