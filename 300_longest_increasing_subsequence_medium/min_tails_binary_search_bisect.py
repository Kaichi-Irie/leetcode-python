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
        subsequence_min_tails = []
        for num in nums:
            index_to_insert = bisect.bisect_left(subsequence_min_tails, num)
            if index_to_insert == len(subsequence_min_tails):
                subsequence_min_tails.append(num)
            else:
                subsequence_min_tails[index_to_insert] = num
        return len(subsequence_min_tails)


# @lc code=end
