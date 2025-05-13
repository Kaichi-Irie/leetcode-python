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

        # cumsum[i] = sum(nums[:i])
        cumsum = [0] * (N + 1)
        for i in range(N):
            cumsum[i + 1] = cumsum[i] + nums[i]
        min_cumsum = [0] * (N + 1)
        for i in range(1, N + 1):
            min_cumsum[i] = min(min_cumsum[i - 1], cumsum[i])

        INF = -pow(10, 4) - 9
        ans = INF
        for i in range(1, N + 1):
            ans = max(ans, cumsum[i] - min_cumsum[i - 1])
        return ans


# @lc code=end
