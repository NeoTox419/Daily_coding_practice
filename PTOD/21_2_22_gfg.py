#problem name: Find H index
'''
-------------------- INTUITION --------------------
The H-index is the maximum number H such that the researcher 
has at least H papers with at least H citations each.

Think of it this way:
- If we sort the citations in descending order,
- We check how many papers have citations >= their position index.

Example:
citations = [3, 0, 6, 1, 5]
After sorting (descending):
[6, 5, 3, 1, 0]

Now check:
index 1 → citation 6 >= 1  ✓
index 2 → citation 5 >= 2  ✓
index 3 → citation 3 >= 3  ✓
index 4 → citation 1 >= 4  ✗

So maximum valid H = 3

-------------------- APPROACH --------------------
1. Sort the citations array in descending order.
2. Traverse through the sorted list.
3. For each index i:
        if citations[i] >= i + 1
            update h = i + 1
4. Return the maximum valid h found.

Time Complexity: O(n log n)  (due to sorting)
Space Complexity: O(1)       (if sorting in-place)
---------------------------------------------------
'''

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        
        h = 0
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
                
        return h