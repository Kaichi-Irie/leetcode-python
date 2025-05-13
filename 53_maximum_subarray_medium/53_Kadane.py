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
        # Kadane's Algorithm
        # dp[end] := max{A[begin]+...+A[end]| begin = 0,...,end-1}
        # と定める．つまりdp[end]は，部分配列A[:i+1]に対し，A[end]を必ず含むような区間についての区間和の最大値を与える．
        # 最後に求める答えは max(dp)
        dp = [0] * N
        dp[0] = nums[0]
        max_till_now = nums[0]
        for i in range(1, N):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_till_now = max(max_till_now, dp[i])
        return max_till_now


# @lc code=end
