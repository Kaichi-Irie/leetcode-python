#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        # cumsum[r] = sum(nums[:r])
        cumsum = [0] * (N + 1)
        for r in range(1, N + 1):
            cumsum[r] = cumsum[r - 1] + nums[r - 1]

        INF = -pow(10, 4) - 9
        ans = INF
        for r in range(1, N + 1):
            for l in range(0, r):
                # sum(nums[l:r])
                ans = max(ans, cumsum[r] - cumsum[l])
        return ans


# @lc code=end
