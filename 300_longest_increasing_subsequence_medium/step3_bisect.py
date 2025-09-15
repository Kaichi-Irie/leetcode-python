#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        tails = []
        for num in nums:
            index = bisect.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
                continue
            tails[index] = min(tails[index], num)
        return len(tails)


# @lc code=end
