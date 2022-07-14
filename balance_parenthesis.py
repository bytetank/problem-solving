

"""
Given a set of open and closed parenthesis. Find whether input is valid or not

[{}]

"""

class Solution:

    def __init__(self):
        self.parenthesis_set = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        self.stack = []

    def balance_parenthesis(self, string: str) -> bool:
        if len(string) == 1:
            return False
        for char in string:
            if char in self.parenthesis_set.values():
                self.stack.append(char)
            elif self.stack[-1] == self.parenthesis_set[char]:
                self.stack.pop()
            else:
                return False
        if self.stack:
            return False
        else:
            return True


if __name__ == "__main__":
    soln = Solution()
    print(soln.balance_parenthesis("[{()}"))


