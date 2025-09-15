#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        left_max_lengths = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    left_max_lengths[i] = max(
                        left_max_lengths[i], left_max_lengths[j] + 1
                    )

        return max(left_max_lengths)


# @lc code=end
