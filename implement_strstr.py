"""
Leet Code Problem
        https://leetcode.com/problems/implement-strstr/
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        last_haystack_ptr = 0
        potential_index = -1
        while last_haystack_ptr < len(haystack):
            if last_haystack_ptr + len(needle) > len(haystack):
                return -1
            for j in range(len(needle)):
                if haystack[last_haystack_ptr + j] == needle[j]:
                    potential_index = last_haystack_ptr
                    continue
                else:
                    last_haystack_ptr += 1
                    break
            else:
                break
        return potential_index

soln = Solution()
print(soln.strStr("hello", "ll"))
