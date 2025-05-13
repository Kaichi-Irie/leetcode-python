#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return nums[0]

        # dp[i]: 1,...,i番目までの家を対象にしたときの，盗める金額の最大値．
        # Memory O(1)解法
        pre = nums[0]
        curr = max(pre, nums[1])
        for i in range(2, N):
            tmp = curr
            curr = max(curr, pre + nums[i])
            pre = tmp
        return curr


# @lc code=end
