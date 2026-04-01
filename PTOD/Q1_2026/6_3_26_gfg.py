#porblem name: Smallest window containing all characters
'''
INTUITION
We need to find the smallest substring in string `s` that contains
all characters of string `p`, including duplicates.

Example:
s = "ADOBECODEBANC"
p = "ABC"
The smallest substring containing A, B, and C is "BANC".

A brute-force approach would check every substring of s and see
if it contains all characters of p, but that would be O(n^3) in
the worst case and is inefficient.

APPROACH (Sliding Window + Frequency Map)
1. First store the frequency of each character of `p` in a dictionary.
2. Use two pointers (left and right) to represent a sliding window
    over string `s`.
3. Expand the right pointer to include characters into the window.
4. Maintain a counter `formed` to track how many required characters
    have been satisfied.
5. Once all characters of `p` are present in the window, try to shrink
    the window from the left to get the minimum valid substring.
6. Keep updating the best (smallest) window found.
7. Continue until the right pointer reaches the end of `s`.

TIME COMPLEXITY
O(n + m)
n = length of s
m = length of p

SPACE COMPLEXITY
O(k) where k is the number of unique characters in p.
'''
class Solution:
    def minWindow(self, s, p):
        from collections import Counter

        if not s or not p:
            return ""

        need = Counter(p)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]