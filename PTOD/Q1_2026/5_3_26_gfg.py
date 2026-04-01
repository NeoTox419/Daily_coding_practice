#porblem name: Longest Substring with K Uniques
'''
Intuition:
We need the longest substring that contains exactly k distinct characters.
A brute force approach would check all substrings and count distinct characters,
but that would take O(n^2) time and is inefficient.

Since we are dealing with substrings (continuous segments), a sliding window
approach works well. We expand the window to the right and track how many
distinct characters are inside the window.

Approach:
1. Use two pointers (left and right) to maintain a sliding window.
2. Maintain a dictionary (or hashmap) to store character frequencies in the window.
3. Expand the window by moving the right pointer and updating the frequency.
4. If the number of distinct characters becomes greater than k, shrink the window
    from the left until the distinct count becomes <= k.
5. Whenever the number of distinct characters equals k, update the maximum length.
6. If no substring with exactly k distinct characters exists, return -1.

Time Complexity: O(n)
Each character enters and leaves the window at most once.

Space Complexity: O(k)
For storing at most k characters in the hashmap.
'''
class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        freq = {}
        max_len = -1

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len