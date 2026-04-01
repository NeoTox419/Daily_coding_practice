# Problem Name: Maximum People Visible in a Line
'''
Intuition:
For any person i, they can see people on the left and right.
A person j is visible to i if:
  1) height[j] < height[i]
  2) There is no person k between i and j with height[k] >= height[i]

Key observation:
For a fixed person i, once we encounter someone with height >= height[i]
in a direction, visibility in that direction stops.

Brute force (checking every i and expanding left/right) would be O(n^2).
We want something more efficient.

Approach:
Use a monotonic stack idea.
For each index i, we count how many people are visible to the left
until a blocking person (height >= arr[i]) appears.
Similarly, count visible people to the right.

Since each person can always see themselves, we add 1.

We do this by:
- For each i, scan left until blocked
- For each i, scan right until blocked
This works in O(n^2) worst-case, but constraints for this problem
typically allow it, and the logic stays very clear and correct.
'''
class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            count = 1  # person can always see themselves

            # look to the left
            for j in range(i - 1, -1, -1):
                if arr[j] < arr[i]:
                    count += 1
                else:
                    break  # blocked by someone taller or equal

            # look to the right
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    count += 1
                else:
                    break  # blocked by someone taller or equal

            ans = max(ans, count)

        return ans
