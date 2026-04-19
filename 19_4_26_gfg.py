#Problem name: Check for Power
'''
Intuition:
A number y is a power of x if we can write y = x^k for some integer k >= 0.
Instead of calculating powers, we repeatedly divide y by x.

If:
- y becomes 1 → it means y = x^k → return True
- y is not divisible by x at any step → return False

Approach:
1. Handle edge cases:
    - If y == 1 → always True (x^0 = 1)
    - If x == 1 → only True when y == 1
2. While y is divisible by x:
        keep dividing y by x
3. If y becomes 1 → return True else False
'''
class Solution:
    def isPower(self, x, y):
        # Edge case
        if y == 1:
            return True
        
        if x == 1:
            return y == 1

        # Keep dividing y by x
        while y % x == 0:
            y //= x

        return y == 1