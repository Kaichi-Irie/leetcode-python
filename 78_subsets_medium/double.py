#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = [[]]
        for num in nums:
            subsets_containing_num = [subset + [num] for subset in all_subsets]
            all_subsets.extend(subsets_containing_num)
        return all_subsets

# @lc code=end
