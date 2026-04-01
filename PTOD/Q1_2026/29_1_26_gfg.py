'''
Problem Name: Stream First Non-repeating

Intuition:
For each prefix of the string, we need the first character that has
appeared exactly once so far.
As we process characters from left to right, we must:
1. Keep track of how many times each character appears.
2. Maintain the order of characters to know which non-repeating
   character appears first.
A queue helps us preserve order, while a frequency array helps us
identify repeating characters efficiently.

Approach:
1. Use a frequency array of size 26 for lowercase letters.
2. Use a queue to store characters in the order they appear.
3. Traverse the string character by character:
   - Update the frequency of the character.
   - Add the character to the queue.
   - Remove characters from the front of the queue if their
     frequency is greater than 1.
4. After processing each character:
   - If the queue is not empty, the front is the first non-repeating character.
   - Otherwise, append '#' to the result.
5. Return the final result as a string.
'''
class Solution:
	def firstNonRepeating(self, s):
		from collections import deque
		
		freq = [0] * 26
		q = deque()
		result = []
		
		for ch in s:
			freq[ord(ch) - ord('a')] += 1
			q.append(ch)
			
			while q and freq[ord(q[0]) - ord('a')] > 1:
				q.popleft()
			
			if q:
				result.append(q[0])
			else:
				result.append('#')
		
		return ''.join(result)
