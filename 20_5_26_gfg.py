#porblem name:Product Pair
class Solution:
    def isProduct(self, arr, target):
        '''
        Intuition:
        We need to check whether there exists any pair in the array
        whose product equals the given target.

        A brute force solution would check every pair using two loops,
        but that would take O(n^2) time.

        Instead, we can optimize using a set:
        - For every number x in the array:
            We need another number y such that:
                    x * y = target
                =>  y = target // x

        If y has already appeared before, then we found a valid pair.

        Special Cases:
        1. If x = 0:
            - Product can only become target if target is also 0.
            - So for target = 0, at least two zeros OR one zero with any number works.
              While traversing, if target == 0 and we already saw a zero,
              we return True.

        2. target must be divisible by x,
           otherwise y will not be an integer.

        Approach:
        - Maintain a set of visited numbers.
        - Traverse the array:
            * Handle zero separately.
            * If target % x == 0:
                  needed = target // x
              Check if needed exists in visited.
            * Add current number into visited.
        - If no pair found, return False.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        visited = set()

        for num in arr:

            # Handle zero separately
            if num == 0:
                if target == 0:
                    return True

            else:
                # Check if num can divide target
                if target % num == 0:
                    needed = target // num

                    if needed in visited:
                        return True

            visited.add(num)

        return False