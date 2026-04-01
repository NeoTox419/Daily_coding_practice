#problem name: Move All Zeors to End
'''
INTUITION:
The problem asks us to move all zeros to the end of the array 
while keeping the relative order of non-zero elements the same.

This means:
- We cannot sort the array.
- We must preserve order.
- We must do it in-place (no extra array allowed).

If we observe carefully, we just need to shift all non-zero 
elements forward and then fill the remaining positions with zeros.


APPROACH:
1. Maintain a pointer `insert_pos` to track where the next non-zero 
element should be placed.

2. Traverse the array:
- If current element is non-zero:
    • Swap it with the element at `insert_pos`
    • Increment `insert_pos`
    
3. By doing this:
- All non-zero elements move to the front in order.
- All zeros automatically shift to the end.

4. Time Complexity: O(n)
5. Space Complexity: O(1) (in-place)
'''
class Solution:    
    def pushZerosToEnd(self, arr):
        insert_pos = 0  # Position to place next non-zero element
        
        # Move all non-zero elements to the front
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
                insert_pos += 1
        
        return arr