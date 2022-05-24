"""

Leet Code Problem
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted
"""
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        prev_elem = nums[0]
        last_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] != prev_elem:
                prev_elem = nums[idx]
                last_idx += 1
                if last_idx != idx:
                    nums[last_idx] = nums[idx]
                    nums[idx] = "_"
            else:
                nums[idx] = "_"
        print(nums)
        return last_idx + 1


soln = Solution()
print(soln.removeDuplicates([0,1,3,4]))
