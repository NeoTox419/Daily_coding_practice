#problem name: Check if All Bits Set
class Solution:
    def isBitSet(self, n):
        '''
        Intuition:
        A number has all bits set if its binary representation contains only 1s.
        
        Examples:
        1  -> 1
        3  -> 11
        7  -> 111
        15 -> 1111
        
        Observation:
        Numbers with all bits set follow this property:
        
            n & (n + 1) == 0
        
        Why?
        If n = 111...111 in binary,
        then n + 1 = 1000...000
        
        Performing AND between them gives 0.
        
        Approach:
        1. Compute (n & (n + 1))
        2. If result is 0, all bits are set.
        3. Otherwise, at least one bit is unset.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        '''
        
        return n > 0 and (n & (n + 1)) == 0