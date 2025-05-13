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

        INF = pow(10, 4) + 9
        ans = -INF
        for l in range(0, N):
            cursum = 0
            for r in range(l + 1, N + 1):
                cursum += nums[r - 1]
                # sum(nums[l:r])
                ans = max(ans, cursum)

        return ans


# @lc code=end
