#Problem name: Wifi Range
class Solution:
    def wifiRange(self, s, x):
        '''
        Intuition:
        Each router placed at index i can cover rooms from:
            i - x  to  i + x
        
        Instead of checking every room against every router
        (which would be inefficient), we can directly mark
        all rooms covered by each router.

        Approach:
        1. Create a coverage array initialized with False.
        2. Traverse the string:
              - If s[i] == '1', calculate its coverage range.
              - Mark all rooms in that range as covered.
        3. After processing all routers, check whether every
           room is covered.
        4. If any room is uncovered, return False.
           Otherwise return True.

        Time Complexity:
            O(n * x) in worst case

        Space Complexity:
            O(n)
        '''

        n = len(s)

        # coverage[i] = True means room i is covered
        coverage = [False] * n

        # Mark coverage for every router
        for i in range(n):
            if s[i] == '1':

                # Calculate left and right limits
                left = max(0, i - x)
                right = min(n - 1, i + x)

                # Mark covered rooms
                for j in range(left, right + 1):
                    coverage[j] = True

        # Check if every room is covered
        for room in coverage:
            if not room:
                return False

        return True