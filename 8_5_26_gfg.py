#Problem name: Remove Invalid Parentheses
class Solution:
    def validParenthesis(self, s):
        '''
        Intuition:
        ----------
        We need to remove the minimum number of invalid parentheses so that
        the final string becomes valid.

        A brute force approach would generate all possible removals and check
        validity, but that becomes very expensive.

        Since we need the MINIMUM removals, Breadth First Search (BFS) is ideal:
        - At each level, remove exactly one parenthesis from every string.
        - The first level where we find valid strings guarantees minimum removals.
        - We stop exploring deeper levels after finding valid strings.

        We also need:
        - distinct answers  -> use a set
        - lexicographical order -> sort before returning


        Approach:
        ---------
        1. Create a helper function `is_valid()`:
           - Traverse the string.
           - Increase count for '('
           - Decrease count for ')'
           - If count becomes negative, string is invalid.
           - At the end count must be 0.

        2. Use BFS:
           - Start with original string.
           - For every string:
                a) Check validity.
                b) If valid -> store answer.
                c) Otherwise remove one parenthesis at every position
                   and push new strings into queue.

        3. Once valid strings are found at a level:
           - Do not generate further levels.
           - This ensures minimum removals.

        4. Return sorted list of valid strings.
        '''

        from collections import deque

        # Helper function to check if parentheses are valid
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    # More closing brackets than opening
                    if count < 0:
                        return False

            return count == 0

        # BFS initialization
        queue = deque([s])
        visited = set([s])

        ans = []
        found = False

        while queue:
            current = queue.popleft()

            # Check if current string is valid
            if is_valid(current):
                ans.append(current)
                found = True

            # If valid strings found at current level,
            # do not generate next level
            if found:
                continue

            # Generate next states by removing one parenthesis
            for i in range(len(current)):

                # Only remove parentheses
                if current[i] not in '()':
                    continue

                next_string = current[:i] + current[i+1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        # Return lexicographically sorted distinct results
        return sorted(set(ans))