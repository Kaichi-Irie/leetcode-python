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
        zero_cnt = 0
        ptr = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
                continue
            nums[ptr] = n
            ptr += 1
        assert ptr + zero_cnt == len(nums)
        for i in range(ptr, ptr + zero_cnt):
            nums[i] = 0


# @lc code=end
