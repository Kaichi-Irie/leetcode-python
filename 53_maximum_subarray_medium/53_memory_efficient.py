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
        cumsum = 0
        min_cumsum = 0
        INF = -pow(10, 4) - 9
        ans = INF
        for i in range(N):
            cumsum += nums[i]
            ans = max(ans, cumsum - min_cumsum)
            min_cumsum = min(min_cumsum, cumsum)
        ans = max(ans, cumsum)
        return ans


# @lc code=end
