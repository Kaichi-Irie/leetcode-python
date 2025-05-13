#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
import functools


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        @functools.cache
        def solve(n):
            if n == 0:
                raise ValueError()
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            return max(solve(n - 1), solve(n - 2) + nums[n - 1])

        return solve(N)


# @lc code=end
