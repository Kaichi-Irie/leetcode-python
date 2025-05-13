#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        def solve(L, R):
            assert 0 <= L <= R <= N
            mid = (R + L) // 2
            if R - L == 0:
                return -inf

            left_sum = 0
            cumsum = 0
            for i in range(mid - 1, L - 1, -1):
                cumsum += nums[i]
                left_sum = max(left_sum, cumsum)

            right_sum = 0
            cumsum = 0
            for i in range(mid + 1, R):
                cumsum += nums[i]
                right_sum = max(right_sum, cumsum)

            val1 = left_sum + nums[mid] + right_sum
            val2 = solve(L, mid)
            val3 = solve(mid + 1, R)
            return max(val1, val2, val3)

        return solve(0, N)


# @lc code=end
