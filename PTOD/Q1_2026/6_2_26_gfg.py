'''
------------------------------------------------------------
Intuition:
------------------------------------------------------------
We want to pick exactly one element from each of the three arrays
such that the difference between the maximum and minimum element
in the chosen triplet is as small as possible.

Brute force would be to try all possible triplets, but that would
take O(n^3) time, which is inefficient.

A better idea:
- If the arrays are sorted, we can use a three-pointer technique.
- At any point, we look at one element from each array.
- The current difference is max(a[i], b[j], c[k]) - min(a[i], b[j], c[k]).
- To potentially reduce this difference, we should move the pointer
  that currently points to the minimum element, because increasing
  the minimum might shrink the range.

While doing this:
- Track the minimum difference seen so far.
- If two triplets have the same minimum difference, choose the one
  with the smaller sum of elements.

Finally, print the chosen triplet in decreasing order.


------------------------------------------------------------
Approach:
------------------------------------------------------------
1. Sort arrays a, b, and c.
2. Initialize three pointers i, j, k to 0.
3. Initialize variables to track:
   - best_diff (minimum max-min found so far)
   - best_sum (sum of elements of the best triplet)
   - best_triplet (the actual elements)
4. While none of the pointers goes out of bounds:
   a. Compute current max, min, diff, and sum.
   b. Update best_triplet if:
      - diff < best_diff, or
      - diff == best_diff and sum < best_sum
   c. Move the pointer which points to the minimum element.
5. Sort the best_triplet in decreasing order and return it.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) extra space (ignoring sorting space)


------------------------------------------------------------
Solution:
------------------------------------------------------------
'''
class Solution:
    def smallestDiff(self, a, b, c):
        # Sort all arrays
        a.sort()
        b.sort()
        c.sort()

        i = j = k = 0
        n = len(a)

        best_diff = float('inf')
        best_sum = float('inf')
        best_triplet = None

        # Three pointer traversal
        while i < n and j < n and k < n:
            x, y, z = a[i], b[j], c[k]

            current_max = max(x, y, z)
            current_min = min(x, y, z)
            current_diff = current_max - current_min
            current_sum = x + y + z

            # Update best triplet based on conditions
            if (current_diff < best_diff) or \
               (current_diff == best_diff and current_sum < best_sum):
                best_diff = current_diff
                best_sum = current_sum
                best_triplet = [x, y, z]

            # Move the pointer with the minimum value
            if current_min == x:
                i += 1
            elif current_min == y:
                j += 1
            else:
                k += 1

        # Return the triplet in decreasing order
        best_triplet.sort(reverse=True)
        return best_triplet
