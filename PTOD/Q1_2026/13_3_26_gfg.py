#Porblem Name: Generate IP Addresses
'''
INTUITION
---------
An IP address consists of 4 parts separated by dots:
A.B.C.D

Each part:
- Must be between 0 and 255
- Cannot have leading zeros unless the number itself is 0
- Length of each part can be 1 to 3 digits

Since the string contains only digits, we need to place
3 dots in such a way that the string is divided into 4
valid segments.

Example:
s = "25525511135"

Possible split:
255.255.11.135
255.255.111.35

------------------------------------------------------

APPROACH
--------
1. Use 3 nested loops to decide the positions of the 3 dots.
2. This divides the string into 4 parts:
        part1 = s[0:i]
        part2 = s[i:j]
        part3 = s[j:k]
        part4 = s[k:]

3. Ensure each part:
    - Length between 1 and 3
    - Value <= 255
    - No leading zeros unless the number is exactly "0"

4. If all four parts are valid, construct the IP:
        part1.part2.part3.part4

5. Store it in the result list.

6. If no valid IPs are found, return empty list.
'''
class Solution:
    def generateIp(self, s):

        res = []
        n = len(s)

        def valid(part):
            # length must be 1-3
            if len(part) == 0 or len(part) > 3:
                return False

            # no leading zero
            if part[0] == '0' and len(part) > 1:
                return False

            # must be <= 255
            if int(part) > 255:
                return False

            return True

        # place 3 dots
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    p1 = s[:i]
                    p2 = s[i:j]
                    p3 = s[j:k]
                    p4 = s[k:]

                    if valid(p1) and valid(p2) and valid(p3) and valid(p4):
                        res.append(p1 + "." + p2 + "." + p3 + "." + p4)

        return res