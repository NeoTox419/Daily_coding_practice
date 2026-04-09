#Problem name: Insertion of two sorted arrays
#Intuation
'''
Since both arrays are already sorted, we can take advantage of this property.

Instead of using extra data structures (like sets), we can use a two-pointer technique:
- One pointer for array a
- One pointer for array b

We move through both arrays simultaneously:
- If elements match → it's part of intersection
- If one is smaller → move that pointer forward

To ensure DISTINCT elements:
- Only add element if it’s not already added (avoid duplicates)

This avoids extra space and keeps it efficient.
'''

#Approach:
'''
1. Initialize two pointers i and j at 0
2. Traverse both arrays:
   - If a[i] == b[j]:
        - Add to result if not duplicate
        - Move both pointers
   - If a[i] < b[j]:
        - Move i
   - Else:
        - Move j
3. Return result list
'''

class Solution:
    def intersection(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []

        while i < n and j < m:
            if a[i] == b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return result