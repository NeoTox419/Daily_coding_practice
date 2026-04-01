'''
Problem Name: Number of Valid Parentheses

Intuation:

A valid parentheses string has some very strict rules:
Every "(" must be closed by a ")".
You can never close before you open.
Total number of "(" must equal total number of ")".

So:
If n is odd, it’s impossible to form a valid string → answer is 0.
If n is even, then exactly n/2 opening and n/2 closing brackets are used.
This problem is not about generating strings, but counting them.
This exact counting problem is a classic Catalan Number problem.

Key observation
Let: pairs = n // 2

The number of valid parentheses expressions using pairs pairs is the
pairs-th Catalan number.

'''

'''
Approach:

We’ll use Dynamic Programming:
dp[i] = number of valid parentheses expressions using i pairs
Base case:
dp[0] = 1 (empty string is valid)

Transition:
dp[i] = sum(dp[j] * dp[i - 1 - j]) for j in range(i)

'''

class Solution:
    def findWays(self, n):
        '''
        Step 1: If n is odd, no valid parentheses expression is possible
        because every '(' needs a matching ')'.
        '''
        if n % 2 != 0:
            return 0
        
        #Step 2: Number of pairs of parentheses
        pairs = n // 2
        
        '''
        Step 3: dp[i] will store the number of valid parentheses
        expressions using i pairs of parentheses.
        '''
        dp = [0] * (pairs + 1)
        
        '''
        Step 4: Base case
        There is exactly 1 valid way to form parentheses with 0 pairs:
        the empty string "".
        '''
        dp[0] = 1
        
        '''
        Step 5: Fill the dp array using the Catalan recurrence relation
        
        For each i pairs:
        - Try placing j pairs inside the first '(' ')'
        - Remaining (i - 1 - j) pairs go outside
        - Multiply the number of ways for both parts
        '''
        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        #Step 6: The answer for n length is dp[pairs]
        return dp[pairs]
