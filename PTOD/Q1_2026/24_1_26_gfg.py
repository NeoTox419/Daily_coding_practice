'''
Problem Name: Josephus problem
INTUITION:
This is the classic Josephus problem.
People stand in a circle and every k-th person is eliminated.
Instead of simulating the entire elimination (which is slow for large n),
we observe a pattern:

If we know the survivor position for n-1 people,
we can compute it for n people by shifting the position by k.

The problem becomes smaller step by step until the base case.
'''

'''
APPROACH:
1. Use the Josephus recurrence relation:
      J(1, k) = 0
      J(n, k) = (J(n-1, k) + k) % n
   This gives the survivor position in 0-based indexing.

2. Convert the final result to 1-based indexing by adding 1.

3. Implement this iteratively to avoid recursion overhead.
'''
class Solution:
    def josephus(self, n, k):
        survivor = 0
        for i in range(2, n + 1):
            survivor = (survivor + k) % i
        return survivor + 1
