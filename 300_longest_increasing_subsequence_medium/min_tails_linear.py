#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # min_tails[i] is the minimum number of the tails of increasing subsequences with length (i+1)
        if not nums:
            return 0
        min_tails = [nums[0]]
        for num in nums[1:]:
            if min_tails[-1] < num:
                min_tails.append(num)
                continue
            for i, tail in enumerate(min_tails):
                if num <= tail:
                    min_tails[i] = num
                    break
        return len(min_tails)


# @lc code=end
