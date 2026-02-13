#Problem name: All numbers with specific difference

'''
INTUITION:
We need to count numbers x (1 ≤ x ≤ n) such that:

    x - sum_of_digits(x) ≥ d

Observe:
    x - sum_of_digits(x) is always non-negative.

Instead of checking every number (which would be slow for large n),
we notice something important:

For large enough numbers, x - sum_of_digits(x) becomes large.
Since sum_of_digits(x) grows much slower than x, once we reach
a certain point, all numbers after that will satisfy the condition.

So instead of checking all numbers from 1 to n, we:
1. Find the smallest number 'start' such that:
        start - sum_of_digits(start) ≥ d
2. Then all numbers from start to n will satisfy the condition.

So answer becomes:
        max(0, n - start + 1)

APPROACH:
1. Binary search between 1 and n to find the smallest number
    that satisfies:
        mid - digit_sum(mid) ≥ d
2. If no such number exists, return 0.
3. Otherwise return:
        n - start + 1
4. Digit sum computation takes O(log n).
    Binary search takes O(log n).
    So total complexity is O(log² n).
'''

class Solution:
    def getCount(self, n, d):
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        
        left, right = 1, n
        start = -1
        
        while left <= right:
            mid = (left + right) // 2
            if mid - digit_sum(mid) >= d:
                start = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if start == -1:
            return 0
        
        return n - start + 1
