#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_pos = 0
        for curr_pos, n in enumerate(nums):
            nums[curr_pos] = 0
            if n == 0:
                continue
            nums[last_non_zero_pos] = n
            last_non_zero_pos += 1


# @lc code=end
