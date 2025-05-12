from typing import List

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        if target <= nums[L]:
            return 0
        elif nums[R] < target:
            return N
        while R - L > 1:
            mid = (R + L) // 2
            if target <= nums[mid]:
                R = mid
            else:
                L = mid
        return R


# @lc code=end
