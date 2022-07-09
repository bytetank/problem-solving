"""
Leet Code Problem
        https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""

from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        def recursive_search(low_idx, high_idx):

            mid_idx = (low_idx + high_idx) // 2
            print(low_idx, high_idx, nums[mid_idx])
            if nums[mid_idx] == target:
                return mid_idx
            elif high_idx - low_idx < 1:
                if target < nums[low_idx]:
                    return low_idx
                else:
                    return low_idx + 1
            elif target > nums[mid_idx]:
                return recursive_search(mid_idx + 1, high_idx)
            else:
                return recursive_search(low_idx, mid_idx - 1)
        return recursive_search(left_ptr, right_ptr)


soln = Solution()
print(soln.searchInsert([1, 3], 0))
