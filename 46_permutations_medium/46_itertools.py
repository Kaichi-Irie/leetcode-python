#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
import itertools


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(
            map(
                list,
                list(itertools.permutations(nums)),
            )
        )


# @lc code=end
