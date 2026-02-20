#problem name: Form the largest number.
'''
First Intuition:
If we sort the numbers in descending order and then concatenate them,
we might get the largest number.

But this fails for cases like:
arr = [3, 30]
Descending sort gives: [30, 3]
Concatenation: "303"
But the correct largest number is "330".

So normal numeric sorting does not work.


Approach:
Instead of comparing numbers directly, compare them based on 
string concatenation.

For two numbers a and b:
- Compare "a+b" and "b+a"
- If "a+b" > "b+a", then a should come before b.
- Otherwise, b should come before a.

Steps:
1. Convert all integers to strings.
2. Sort using a custom comparator based on concatenation rule.
3. Join the sorted strings.
4. Edge case: If the largest number is "0", return "0".
'''
class Solution:
    
    def findLargest(self, arr):
        
        
        from functools import cmp_to_key
        
        # Convert integers to strings
        arr = list(map(str, arr))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come before b
            elif a + b < b + a:
                return 1    # b should come before a
            else:
                return 0
        
        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Edge case: if highest value is "0"
        if arr[0] == "0":
            return "0"
        
        # Join and return result
        return ''.join(arr)