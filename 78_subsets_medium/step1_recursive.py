#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [[], nums]
        num = nums[0]
        sub_subsets = self.subsets(nums[1:])
        all_subsets = []
        for subset in sub_subsets:
            all_subsets.append(subset.copy())
            subset.append(num)
            all_subsets.append(subset.copy())
        return all_subsets


# @lc code=end
