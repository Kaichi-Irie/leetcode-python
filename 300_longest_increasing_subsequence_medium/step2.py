#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # max_length[i] is the maximum length of increasing subsequences that ends at nums[i]
        max_lengths = [1] * len(nums)
        for i in range(len(nums)):
            max_previous_length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_previous_length = max(max_previous_length, max_lengths[j])
            max_lengths[i] = max_previous_length + 1
        return max(max_lengths)


# @lc code=end
