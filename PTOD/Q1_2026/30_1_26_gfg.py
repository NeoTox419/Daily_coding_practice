'''
Intuition:
The queue has an even number of elements, so it can be divided into two equal halves.
If we separate the first half and the second half, we can interleave them by
alternately taking elements from each half while maintaining their original order.

Approach:
1. Find the midpoint of the queue.
2. Store the first half and second half separately.
3. Create a new queue by alternately inserting elements from the first half
   and the second half.
4. Return the rearranged queue.
'''
class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        
        temp = deque()
        
        for _ in range(half):
            temp.append(q.popleft())
        
        while temp:
            q.append(temp.popleft())
            q.append(q.popleft())
            