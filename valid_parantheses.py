"""
Leet Code Problem
        https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""
class Solution:
    def __init__(self):
        self.complement_parentheses = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        temp_list = []
        for par in s:
            if par in self.complement_parentheses.values():
                temp_list.append(par)
            else:
                if temp_list and temp_list[-1] == self.complement_parentheses[par]:
                    temp_list.pop()
                else:
                    return False
        if temp_list:
            return False
        else:
            return True




if __name__ == "__main__":
    soln = Solution()
    print(soln.isValid("([{}])"))