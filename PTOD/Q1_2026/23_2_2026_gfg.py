#problem name: Union of Arrays with duplicates
'''
-----------------------------------------------------------
INTUITION:
The union of two arrays means we need all DISTINCT elements
that appear in either array a or array b.

Important points:
- If an element appears multiple times, we include it only once.
- Order does not matter (driver will sort before printing).

APPROACH:
1. Create an empty set.
   -> A set automatically stores only unique elements.

2. Traverse array 'a' and add each element to the set.

3. Traverse array 'b' and add each element to the same set.

4. Convert the set back to a list and return it.

Time Complexity:
  O(n + m)  where n = len(a), m = len(b)

Space Complexity:
  O(n + m) in worst case (if all elements are unique)
-----------------------------------------------------------
'''
class Solution:
    def findUnion(self, a, b):
        union_set = set()

        # Add elements of first array
        for num in a:
            union_set.add(num)

        # Add elements of second array
        for num in b:
            union_set.add(num)

        return list(union_set)