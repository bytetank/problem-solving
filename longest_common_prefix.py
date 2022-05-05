"""
Leet Code Problem
        https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List
class Solution:
    def __init__(self):
        self.longest_comm_prefix = ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.longest_comm_prefix = strs[0]
        for i in range(1, len(strs)):
            offset = min(len(self.longest_comm_prefix), len(strs[i]))
            while offset != 0:
                if self.longest_comm_prefix[0: offset] == strs[i][0: offset]:
                    self.longest_comm_prefix = self.longest_comm_prefix[0: offset]
                    break
                else:
                    offset -= 1
            else:
                self.longest_comm_prefix = ""
                break
        return self.longest_comm_prefix


if __name__ == "__main__":
    soln = Solution()
    print(soln.longestCommonPrefix(["racedog", "racedogcar","racedogcar"]))

