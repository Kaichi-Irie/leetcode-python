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
        elif len(nums) == 1:
            return nums[0]

        max_rob_amount_excluding_first = self.rob_houses_linear(nums[1:])
        max_rob_amount_excluding_last = self.rob_houses_linear(nums[: len(nums) - 1])
        return max(max_rob_amount_excluding_first, max_rob_amount_excluding_last)

    def rob_houses_linear(self, nums: list[int]) -> int:
        """
        solve house robber problem when houses are arranged linear (not in a circle)
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        previous_rob_amount = nums[0]
        current_rob_amount = max(previous_rob_amount, nums[1])
        for i in range(2, len(nums)):
            tmp = current_rob_amount
            current_rob_amount = max(current_rob_amount, previous_rob_amount + nums[i])
            previous_rob_amount = tmp
        return max(previous_rob_amount, current_rob_amount)


# @lc code=end
