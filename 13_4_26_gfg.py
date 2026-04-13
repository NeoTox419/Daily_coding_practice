'''
INTUITION:
A palindrome reads the same forward and backward. To get the next smallest
palindrome strictly larger than the given number, we want to minimally
increase the number while maintaining the palindrome property.

Key idea:
1. Mirror the left half of the number onto the right half.
    - This gives the "closest" palindrome.
2. If this mirrored number is already greater than the original,
    that’s our answer.
3. Otherwise, we need to increment the middle (like handling carry)
    and then mirror again.

APPROACH:
1. Let n = length of num.
2. Create a copy of num → pal.
3. Mirror left half to right:
    - pal[i] = pal[n-1-i] for all i < n//2
4. Compare pal with original num:
    - If pal > num → return pal
5. Else:
    - Add 1 to the middle:
        - If n is odd → increment middle element
        - If n is even → start from middle-left
    - Propagate carry towards left
6. After increment, mirror left to right again.
7. Return the result.
'''

class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        pal = num[:]  # copy

        # Step 1: mirror left to right
        for i in range(n // 2):
            pal[n - 1 - i] = pal[i]

        # Step 2: check if palindrome is already greater
        if pal > num:
            return pal

        # Step 3: handle increment (carry)
        carry = 1
        mid = n // 2

        # If odd length, increment middle
        if n % 2 == 1:
            pal[mid] += 1
            carry = pal[mid] // 10
            pal[mid] %= 10
            left = mid - 1
        else:
            left = mid - 1

        # Propagate carry to left side
        while left >= 0 and carry:
            pal[left] += carry
            carry = pal[left] // 10
            pal[left] %= 10
            left -= 1

        # Step 4: mirror again
        for i in range(n // 2):
            pal[n - 1 - i] = pal[i]

        return pal