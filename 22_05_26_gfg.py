class Solution:
    '''
    Intuition:
    ----------
    Both players always follow a greedy strategy:
    - At every turn, they compare the first and last coin.
    - They remove the larger valued coin.
    
    Instead of simulating two different players separately,
    we can observe that after every move exactly one coin is removed.
    
    Since the process continues until only one coin remains,
    we repeatedly remove the larger coin from either end.
    
    The coin that survives at the end is the answer.
    
    
    Approach:
    ----------
    1. Use two pointers:
       - i -> start of array
       - j -> end of array
    
    2. While more than one coin exists:
       - Compare arr[i] and arr[j]
       - Remove the larger coin:
            * if arr[i] >= arr[j], move i forward
            * else move j backward
    
    3. When i == j, only one coin remains.
    
    4. Return arr[i].
    
    
    Time Complexity:
    ----------------
    O(N) because each move removes one coin.
    
    Space Complexity:
    -----------------
    O(1) auxiliary space.
    '''
    
    def coin(self, arr):
        i = 0
        j = len(arr) - 1

        # Continue until only one coin remains
        while i < j:
            # Greedily remove the larger coin
            if arr[i] >= arr[j]:
                i += 1
            else:
                j -= 1

        # Last remaining coin
        return arr[i]