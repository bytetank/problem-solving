"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        result = ""
        diff = len(a) - len(b)
        if diff > 0:
            b = "0" * diff + b
        elif diff < 0:
            a = "0" * abs(diff) + a
        for i in range(len(a)-1, -1, -1):
            sum = int(a[i]) + int(b[i]) + int(carry)
            result = ("1" if sum%2 else "0") + result
            if sum >= 2:
                carry = "1"
            else:
                carry = "0"
        return result if carry == "0" else "1" + result
    

soln = Solution()
print(soln.addBinary("0", "0"))