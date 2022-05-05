"""
Leet Code Problem
        https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution:

    def __init__(self):
        self.highest_10_power = 0
        self.start_10_power = 0
    ### Solution 1
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        while x // pow(10, self.highest_10_power) >= 1:
            self.highest_10_power += 1
        self.highest_10_power -= 1
        reversed_number = self.__reverse_number(x, self.highest_10_power, self.start_10_power)
        if x == reversed_number:
            return True
        else:
            return False

    # Reversing number
    def __reverse_number(self, num: int, highest_power: int, start_power: int):
        if highest_power == 0:
            return num * pow(10, self.highest_10_power)
        else:
            quotient, remainder = divmod(num, pow(10, highest_power))
            return (quotient * pow(10, start_power)) + self.__reverse_number(remainder, highest_power - 1, start_power+1)
    '''

    ### Solution 2

    def isPalindrome(self, x: int) -> bool:
        if x // 10 == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        reversed_number = 0
        while x > reversed_number:
            current_op_remainder = x % 10
            reversed_number = reversed_number * 10 + current_op_remainder
            x //= 10

        if (x == reversed_number) or x == (reversed_number // 10):
            return True
        else:
            return False


if __name__ == "__main__":
    soln = Solution()
    print(soln.isPalindrome(9))
