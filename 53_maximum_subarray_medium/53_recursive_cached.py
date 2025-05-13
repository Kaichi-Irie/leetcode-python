#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
from functools import cache
from math import inf


# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else -inf
            return max(
                nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False)
            )

        return solve(0, False)


# @lc code=end
