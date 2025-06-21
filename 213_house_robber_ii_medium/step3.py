#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        rob_amount_excluing_first = self._rob_houses_linear(nums[1:])
        rob_amount_excluing_last = self._rob_houses_linear(nums[: len(nums) - 1])

        max_rob_amount = max(rob_amount_excluing_first, rob_amount_excluing_last)
        return max_rob_amount

    def _rob_houses_linear(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # dp[i]: the maximum robbed amount from first i houses;  0, ..., i-1
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # use 1-dimensional dynamic programming for efficient memory,
        previous_max_rob_amount = nums[0]
        max_rob_amount = max(previous_max_rob_amount, nums[1])
        for num in nums[2:]:
            tmp = max_rob_amount
            max_rob_amount = max(max_rob_amount, previous_max_rob_amount + num)
            previous_max_rob_amount = tmp

        return max_rob_amount


# @lc code=end
