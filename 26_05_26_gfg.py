#Problem name: Minimum toggle to Partition

class Solution:
    def minToggle(self, arr):
        '''
        Intuition:
        We want the final array in the form:
            0 0 0 ... 1 1 1

        That means there exists some partition index:
        - left side should contain only 0s
        - right side should contain only 1s

        For every possible partition:
            toggles needed =
                (number of 1s on left side) +
                (number of 0s on right side)

        Instead of checking every side repeatedly,
        we process the array once.

        Maintain:
        - ones_left  -> how many 1s seen so far
        - zeros_right -> how many 0s remain on right side

        Initially:
        - left side empty
        - right side contains all elements

        For each partition position:
            answer = min(answer, ones_left + zeros_right)

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        # count total zeros initially on the right side
        zeros_right = arr.count(0)

        ones_left = 0

        # partition before first element
        ans = zeros_right

        for num in arr:

            # move current element from right part to left part
            if num == 0:
                zeros_right -= 1
            else:
                ones_left += 1

            # toggles needed for current partition
            ans = min(ans, ones_left + zeros_right)

        return ans