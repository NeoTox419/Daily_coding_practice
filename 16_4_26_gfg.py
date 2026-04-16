#problem name: Implement Atoi
'''
INTUITION:
We simulate how atoi() works manually:
- Ignore leading spaces
- Detect sign (+ or -)
- Read digits until a non-digit appears
- Build the number step by step
- Handle overflow while building (not after)

APPROACH:
1. Strip leading whitespaces using pointer (not built-in strip).
2. Check for sign:
    - '+' => positive
    - '-' => negative
3. Traverse character by character:
    - If digit → update result = result * 10 + digit
    - If non-digit → stop parsing
4. Handle overflow BEFORE adding digit:
    - If result > (INT_MAX - digit) // 10 → overflow
5. Return final number with sign applied.

EDGE CASES:
- Empty string → 0
- Only spaces → 0
- No digits → 0
- Overflow → clamp to [-2^31, 2^31-1]
'''
class Solution:
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Handle overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result