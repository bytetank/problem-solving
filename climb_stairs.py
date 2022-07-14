"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


class Solution:

    def __init__(self):
        self.result = 0
        self.previous_steps_searched = {}

    def climbStairs(self, n: int) -> int:
        return self.other_solution(n)

    def recursive_search(self, n):
        if n == 1: return 1
        if n == 2: return 2
        prev_step_data = self.previous_steps_searched.get(n, None)
        if prev_step_data:
            return prev_step_data
        self.result = self.recursive_search(n - 1) + self.recursive_search(n - 2)
        self.previous_steps_searched.setdefault(n, self.result)
        return self.result

    def other_solution(self, n):
        pre, curr, temp = 1, 1, 0
        for i in range(1, n):
            temp = curr
            curr += pre
            pre = temp
            print(temp, curr, pre)
        return curr

soln = Solution()
print(soln.climbStairs(5))
