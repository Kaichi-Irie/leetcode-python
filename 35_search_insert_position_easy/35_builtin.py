from bisect import bisect_left
from typing import List

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        return idx


# @lc code=end
