'''
INTUITION
---------
We are given a binary array and we can flip any subarray of length k.
Flipping means converting 0 → 1 and 1 → 0.

Our goal is to make the entire array contain only 1's using the minimum
number of flips.

Key observation:
We process the array from left to right. If we encounter a 0 at position i,
the only way to make it 1 is to flip a subarray starting at i (since earlier
positions cannot affect it anymore).

So whenever we see a 0 at index i:
    - We perform a flip operation on the subarray [i, i+k-1]

However, if i + k > n, then we cannot flip because the subarray would exceed
the array bounds. In that case it is impossible → return -1.

Naively flipping k elements every time would be O(n*k), which can be slow.
Instead, we keep track of active flips using a helper array.

We maintain:
    flip[i] → whether a flip starts at index i
    current_flips → number of flips affecting current index

If current_flips is even → bit stays same
If current_flips is odd → bit is inverted

Before processing index i we remove the flip effect that ended at i-k.

APPROACH
--------
1. Traverse the array from left to right.
2. Maintain how many flips currently affect the index.
3. If the effective value of arr[i] is 0:
        - we must flip starting here
        - increment operation count
        - mark flip[i] = 1
        - increase current_flips
4. Remove flip effect when it goes out of window (i >= k).
5. If we need a flip but i + k > n → return -1.
6. Return total operations.
'''

class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = [0] * n
        current_flips = 0
        operations = 0

        for i in range(n):
            if i >= k:
                current_flips -= flip[i - k]

            if (arr[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flip[i] = 1
                current_flips += 1
                operations += 1

        return operations

        