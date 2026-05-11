#Problem name: Palindrome pairs
class Solution:
    def palindromePair(self, arr):
        '''
        Intuition:
        -----------
        We need to check whether there exists two different strings
        such that their concatenation becomes a palindrome.

        A brute force idea is:
        - Try every pair (i, j)
        - Form arr[i] + arr[j]
        - Check if it is palindrome

        If any pair forms a palindrome, return True.

        ------------------------------------------------------------

        Approach:
        ----------
        1. Traverse all pairs using two nested loops.
        2. Skip when i == j because indices must be different.
        3. Concatenate arr[i] + arr[j].
        4. Check if the concatenated string equals its reverse.
        5. If yes, return True immediately.
        6. After checking all pairs, return False.

        Time Complexity:
        ----------------
        O(n^2 * k)
        where:
        - n = number of strings
        - k = average length of string

        Space Complexity:
        -----------------
        O(k) for temporary concatenated string.
        '''

        n = len(arr)

        for i in range(n):
            for j in range(n):

                # indices must be different
                if i != j:

                    # concatenate strings
                    temp = arr[i] + arr[j]

                    # check palindrome
                    if temp == temp[::-1]:
                        return True

        return False