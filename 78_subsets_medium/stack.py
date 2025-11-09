#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []
        stack = [([], 0)]
        while stack:
            subset, index = stack.pop()
            if index == len(nums):
                all_subsets.append(subset[:])
                continue
            stack.append((subset, index + 1))
            stack.append((subset + [nums[index]], index + 1))
        return all_subsets

# @lc code=end
