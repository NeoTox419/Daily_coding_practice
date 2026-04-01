#problem name:Consecutive 1's not allowed
'''
INTUITION:
We want to count binary strings of length n with NO consecutive 1s.

Think about building the string step by step:
At each position, we can place:
- '0' → no restriction
- '1' → only if previous was NOT '1'

So the constraint depends on the previous character.

This naturally leads to splitting the problem:
- Count strings ending with 0
- Count strings ending with 1

APPROACH:
Let:
end0[i] = number of valid strings of length i ending with '0'
end1[i] = number of valid strings of length i ending with '1'

Transitions:
- If we add '0', we can append it to ANY valid string:
        end0[i] = end0[i-1] + end1[i-1]

- If we add '1', previous must be '0':
        end1[i] = end0[i-1]

Total:
        total[i] = end0[i] + end1[i]

Base case:
        n = 1:
        end0 = 1 ("0")
        end1 = 1 ("1")

This forms a Fibonacci-like recurrence:
        total[n] = total[n-1] + total[n-2]

We can optimize space using two variables.

TIME: O(n)
SPACE: O(1)
'''
class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2

        # end0 and end1 for length 1
        end0 = 1
        end1 = 1

        for i in range(2, n + 1):
            new_end0 = end0 + end1
            new_end1 = end0

            end0 = new_end0
            end1 = new_end1

        return end0 + end1