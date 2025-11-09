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

        max_lengths_so_far = [1] * len(nums)

        for i in range(1, len(nums)):
            length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    length = max(length, max_lengths_so_far[j])
            max_lengths_so_far[i] = length + 1
        return max(max_lengths_so_far)


# @lc code=end
