#Problem name: Print Diagonally
'''
INTUITION:
In an n x n matrix, elements on the same anti-diagonal have the same sum of indices (i + j).
For example:
- First anti-diagonal → i+j = 0
- Next → i+j = 1
- ...
- Last → i+j = 2n-2

So, if we iterate over all possible values of (i + j), we can collect elements belonging
to each anti-diagonal.

APPROACH:
1. Let n = size of matrix.
2. Loop for diagonal sum 'd' from 0 to 2*n - 2.
3. For each 'd', iterate row index i from 0 to n-1:
    - Compute j = d - i
    - If j is within bounds (0 <= j < n), include mat[i][j]
4. Append collected elements in order.
5. Return final list.
'''
def diagView(self, mat):
    n = len(mat)
    result = []

    for d in range(2 * n - 1):
        for i in range(n):
            j = d - i
            if 0 <= j < n:
                result.append(mat[i][j])

    return result